#!/usr/bin/python

import roslib; roslib.load_manifest('asctec_mon')
import rospy
import sys

from asctec_msgs.msg import LLStatus
from asctec_msgs.msg import IMUCalcData
from asctec_msgs.msg import GPSData
from asctec_msgs.msg import CurrentWay
from asctec_msgs.msg import WaypointData
from asctec_msgs.msg import WaypointCommand

import struct
import binascii

WAYPOINT_VEL = 20 # 0..100%

MIN_ALT_REF = -30.0
MAX_ALT_REF =  30.0
MIN_YAW_REF =  0.0
MAX_YAW_REF = 360.0

# if set waypoint is interpreted as absolute coordinates, else relative coords
WPPROP_ABSCOORDS 		= 0x01
# set new height at waypoint
WPPROP_HEIGHTENABLED 	= 0x02
# set new yaw-angle at waypoint (not yet implemented)
WPPROP_YAWENABLED 		= 0x04
# if set, vehicle will not wait for a goto command, but goto this waypoint directly
WPPROP_AUTOMATICGOTO 	= 0x10
# if set, photo camera is triggered when waypoint is reached and time to stay is 80% up (not available on pelican!)
WPPROP_CAM_TRIGGER 		= 0x20

nav_status = 0
waypointList = [
	{'X': 0, 'Y': 10, 'Z': 2},
	{'X': 10, 'Y': 0, 'Z': 2},
	{'X': 0, 'Y': 14, 'Z': 2},
	{'X': 5, 'Y': 5, 'Z': 2}
]

class Waypoint:
	def __init__(self, x=0.0, y=0.0, z=0.0, heading=0.0):
		
		self.wp_number	= 1 # always 1
		self.dummy_1 	= 0 # (don't care)
		self.dummy_2	= 0 # (don't care)
		self.properties	= WPPROP_YAWENABLED + WPPROP_AUTOMATICGOTO
		#self.properties	= WPPROP_AUTOMATICGOTO 
		#WPPROP_HEIGHTENABLED + 
		self.max_speed 	= WAYPOINT_VEL # 0-100%
		self.time 		= 500 # in 1/100th s
		self.pos_acc 	= 1500 # (2m) in mm, how close it can be to be 'at the waypoint'
		
		#Waypoint initialization
		print x, y
		self.X = 		int(x*1000) # [mm]
		self.Y = 		int(y*1000) # [mm]
		
		############################
		# limita referencia de altitude
		if z < MIN_ALT_REF:
			z = MIN_ALT_REF
		if z > MAX_ALT_REF:
			z = MAX_ALT_REF
			
		self.height =	int(z*1000) # [mm]
		print self.height
		############################
		# limita yaw
		if heading < MIN_YAW_REF:
			heading = MIN_YAW_REF
		if heading > MAX_YAW_REF:
			heading = MAX_YAW_REF
		
		self.yaw = 	int(heading*1000) # [deg*1000]
		############################
		self.chksum = 0
		############################
		self.zref = 0
		self.chksum_short = 0
		
	#########################################################################
	# cria waypoint para mandar
	# number: 1..n
	# x, y, z: [m]
	# heading: [deg]
	#########################################################################
	def get_Waypoint(self, zCurrent, zInit):
		
		zCurrent = int(zCurrent*1000) 	# altitude corrente do quadrotor
		zInit = int(zInit*1000)			# altitude inicial dada
		
		# calcula um novo zref baseado na altitude do quadrotor
		zref =  self.height + zInit # referencia relativa a condicao inicial
		print zref
		zref = zref + .2*(zref - zCurrent) # fator de correcao proporcional
		print zref
		# limita referencia de altitude
		if zref < (1000*MIN_ALT_REF):
			zref = (1000*MIN_ALT_REF)
		if zref > (1000*MAX_ALT_REF):
			zref = (1000*MAX_ALT_REF)
		print zref
			
		#print self.height/1000.0, zref/1000.0
		
		# calcula o checksum
		self.chksum = (0xaaaa+self.yaw+ zref +self.time+self.X+self.Y+self.max_speed+self.pos_acc+self.properties+self.wp_number)
		# delimita o checksum
		self.chksum = self.chksum % 65536
		
		#B = unsigned char, H = unsigned short, h = short, 4i = four int's g iiii)
		New_position = struct.Struct('BBHBBHHH4i')

        # '{yaw: 0, height: 5000, time: 500, X: 10000, Y: 0, max_speed: 100, pos_acc: 2500, properties: 16, wp_number: 1, dummy_1: 0, dummy_2: 0, chksum: 61807}'
		self.zref = zref

		checksum = struct.Struct('H')
		checksum = checksum.pack(self.chksum)
		#print "unpack! ",struct.unpack('H', checksum);


		hexstring = binascii.hexlify(checksum)
		hexlist = [hexstring[i:i+2] for i in range(0,len(hexstring), 2)]
		hexlistreversed = list(reversed(hexlist))
		inthexreversed = ''.join(hexlistreversed)
		x = int(hexstring, 16)
		#print "chcksum :",hexstring, "int :", x, " hexlistreversed :", inthexreversed, 16
		self.chksum_short = struct.unpack('H', checksum)[0]


		return New_position.pack(	self.wp_number,		# B = unsigned char
									self.dummy_1,		# B = unsigned char
									self.dummy_2,		# H = unsigned short
									self.properties,	# B = unsigned char
									self.max_speed,		# B = unsigned char
									self.time,			# H = unsigned short
									self.pos_acc,		# H = unsigned short
									self.chksum,		# H = unsigned short (e nao h = short)
									self.X, 			# i = int
									self.Y, 			# i = int
									self.yaw,			# i = int 
									zref) #self.height)		# i = int
										
	#########################################################################
	def show(self):	
		print "x = " + str(self.X) + "\ty = " + str(self.Y) + "\tz = " + str(self.height) + "\tyaw = " + str(self.yaw)

	def generateWPforROSPublish(self):	
		rosCommand = "'{wp_number: "+str(self.wp_number)+", dummy_1: 0, dummy_2: 0, properties: "+str(self.properties)+", max_speed: "+str(self.max_speed)+", time: "+str(self.time)+", pos_acc: "+str(self.pos_acc)+", chksum: "+str(self.chksum_short)+", X: "+str(self.X)+", Y: "+str(self.Y)+", yaw: "+str(self.yaw)+", height: "+str(int(self.zref))+"'}"
		return rosCommand

	def getValuesAsDict(self):
		return {'wp_number': self.wp_number, 'dummy_1': 0, 'dummy_2': 0, 'properties': self.properties, 'max_speed': self.max_speed, 'time': self.time, 'pos_acc': self.pos_acc, 'chksum': self.chksum_short, 'X': self.X, 'Y': self.Y, 'yaw': self.yaw, 'height': self.zref }

	def getWaypointStruct(self):
		wp_data = WaypointData()

		wp_data.wp_number = self.wp_number
		wp_data.dummy_1 = self.dummy_1
		wp_data.dummy_2 = self.dummy_2
		wp_data.properties = self.properties
		wp_data.max_speed = self.max_speed
		wp_data.time = self.time
		wp_data.pos_acc = self.pos_acc
		wp_data.chksum = self.chksum_short
		wp_data.X = self.X
		wp_data.Y = self.Y
		wp_data.yaw = self.yaw
		wp_data.height = self.zref

		return wp_data
	#########################################################################

def gps_callback(data):
    lat_val = float(data.latitude)/float(10**7)
    lon_val = float(data.longitude)/float(10**7)
    height_val = float(data.height)/1000.0
    heading_val = float(data.heading)/1000.0

    print 'Lat: {0:+12.7f}'.format(lat_val)
    print 'Lon: {0:+12.7f}'.format(lon_val)
    print 'Height: {0: 7.3f}m'.format(height_val)
    print 'Heading: {0: 7.3f}'.format(heading_val)

def ll_callback(data):
    battery_val = float(data.battery_voltage_1)/1000.0
    print 'Battery: {0:.3f}V'.format(battery_val)

def currentw_callback(data):
    global nav_status
    nav_status = int(data.navigation_status)
    distance_to_wp = float(data.distance_to_wp)*float(10)

    print 'Nav status: '+str(nav_status)
    print 'Distance to WP in CM: {0:.1f}'.format(distance_to_wp)

def publish_next_waypoint(waypoint_cmd_publisher, waypoint_data_publisher):
    print "PUBLISHING WAYPOINT"

    wp_command = WaypointCommand()
    wp_command.cmd = ">*>wg"
    wp_command.header.stamp = rospy.get_rostime()
    waypoint_cmd_publisher.publish(wp_command)

    current_wp = waypointList.pop(0)
    wp = Waypoint(current_wp['X'], current_wp['Y'], current_wp['Z'], 0)
    wp.get_Waypoint(0, 500)
    #print wp.generateWPforROSPublish()
    waypoint_data = wp.getWaypointStruct()
    waypoint_data.header.stamp = rospy.get_rostime()
    waypoint_data_publisher.publish(waypoint_data)

    print "WAYPOINT PUBLISHED",wp_command, waypoint_data	


def initialize_node():
    rospy.init_node('waypoint_manager')
    
    rospy.Subscriber("asctec/LL_STATUS", LLStatus, ll_callback)
    #rospy.Subscriber("asctec/GPS_DATA", GPSData, gps_callback)
    rospy.Subscriber("asctec/CURRENT_WAY", CurrentWay, currentw_callback)
    
    waypoint_cmd_publisher = rospy.Publisher('/asctec/WAYCOMMAND', WaypointCommand)
    waypoint_data_publisher = rospy.Publisher('/asctec/WAYPOINT', WaypointData)

    rospy.sleep(3)
    r = rospy.Rate(2)



    publish_next_waypoint(waypoint_cmd_publisher, waypoint_data_publisher)
    # r.sleep()

    # count = 0

    # while not rospy.is_shutdown():
    #     count += 1
    #     if(count > 20):
    #         publish_next_waypoint(waypoint_cmd_publisher, waypoint_data_publisher)
    #         count = 0
		
    #     r.sleep()


if __name__ == "__main__":
    initialize_node()
    rospy.spin()