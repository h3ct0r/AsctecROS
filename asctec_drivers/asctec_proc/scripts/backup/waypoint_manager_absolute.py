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
import os
import math
import time
import datetime
import re

WAYPOINT_VEL = 50 # 0..100%

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
lat_val = 0
lon_val = 0
height_val = 5
heading_val = 0
battery_val = 0
distance_to_wp = 0

min_distance_inside_waypoint = 50


hummBaseName = ""
roslaunch_height = 0
height_val_imu = 0
height_delta = 0
# speed in x (E/W) and y(N/S) in mm/s
gps_speedx = 0 
gps_speedy = 0
#Numero de satelites
gps_numSV = 0 

waypointList = []

'''
Campo de futebol pequeno
# X is longitude
# Y is latitude
waypointList = [
	{'X': -43.960432, 'Y': -19.861114, 'Z': 2},
	{'X': -43.960288, 'Y': -19.860861, 'Z': 2},
	{'X': -43.960597, 'Y': -19.861023, 'Z': 2},
	{'X': -43.960338, 'Y': -19.861279, 'Z': 2},
	{'X': -43.960124, 'Y': -19.861234, 'Z': 2}
]
'''

#Campo de futebol grande
# X is longitude
# Y is latitude
#waypointList = [
#	{'X': -43.958376, 'Y': -19.869574, 'Z': 2},
#	{'X': -43.958081, 'Y': -19.869348, 'Z': 2},
#	{'X': -43.957749, 'Y': -19.869736, 'Z': 2},
#	{'X': -43.958048, 'Y': -19.869963, 'Z': 2},
#	{'X': -43.958046, 'Y': -19.869642, 'Z': 2} 
#]

# Small square center of futball field

# waypointList = [
# 	{'X': -43.957929611206055, 'Y': -19.869701638874098, 'Z': 2},
# 	{'X': -43.95807445049285, 'Y': -19.869540196761694, 'Z': 2},
# 	{'X': -43.95796447992324, 'Y': -19.869739476845407, 'Z': 2},
# 	{'X': -43.95811200141907, 'Y': -19.86957551223782, 'Z': 2},
# 	{'X': -43.95800203084946, 'Y': -19.869777314807695, 'Z': 2},
# 	{'X': -43.958149552345276, 'Y': -19.869613350239256, 'Z': 2},
# 	{'X': -19.86981767529084, 'Y': -43.95803689956665, 'Z': 2},
# 	{'X': -43.958187103271484, 'Y': -19.86964866569908, 'Z': 2} 
# ]


#Points in the reitoria
'''
waypointList = [
 	{'X': -43.96395117044449, 'Y': -19.866805746010677, 'Z': 2},
 	{'X': -43.96409064531326, 'Y': -19.866588804171858, 'Z': 2},
 	{'X': -43.96390289068222, 'Y': -19.866505558968868, 'Z': 2},
 	{'X': -43.96387338638306, 'Y': -19.866548442866783, 'Z': 2},
 	{'X': -43.96421402692795, 'Y': -19.866697275128367, 'Z': 2},
 	{'X': -43.964179158210754, 'Y': -19.866737636395566, 'Z': 2},
 	{'X': -43.96384388208389, 'Y': -19.866591326753095, 'Z': 2},
 	{'X': -43.96381437778473, 'Y': -19.866634210627804, 'Z': 2},
 	{'X': -43.964141607284546, 'Y': -19.866777997652502, 'Z': 2},
 	{'X': -43.96399140357971, 'Y': -19.866767907339213, 'Z': 2},
 	{'X': -43.96378755569458, 'Y': -19.86667709449091, 'Z': 2},
 	{'X': -43.963758051395416, 'Y': -19.866719978342427, 'Z': 2},
 	{'X': -43.96395117044449, 'Y': -19.866805746010677, 'Z': 2}
]
'''

#Waypoints Hexagon no Campo de Futebol 1
# waypointList = [{'X': -43.95809590816498, 'Y': -19.869439295357967, 'Z': 2}]
# {'Y': -43.957940340042114, 'X': -19.869525061555223, 'Z': 2},
# {'Y': -43.957892060279846, 'X': -19.869610827706094, 'Z': 2},
# {'Y': -43.958203196525574, 'X': -19.869439295357967, 'Z': 2},
# {'Y': -43.95823001861572, 'X': -19.869484700997592, 'Z': 2},
# {'Y': -43.95791351795196, 'X': -19.8696562332966, 'Z': 2},
# {'Y': -43.957940340042114, 'X': -19.869701638874098, 'Z': 2},
# {'Y': -43.9582622051239, 'X': -19.869525061555223, 'Z': 2},
# {'Y': -43.95828902721405, 'X': -19.86956542210259, 'Z': 2},
# {'Y': -43.95796716213226, 'X': -19.869741999376505, 'Z': 2},
# {'Y': -43.957993984222405, 'X': -19.86978740492944, 'Z': 2},
# {'Y': -43.9583158493042, 'X': -19.869610827706094, 'Z': 2},
# {'Y': -43.95826756954193, 'X': -19.86969659381057, 'Z': 2},
# {'Y': -43.95810127258301, 'X': -19.86978740492944, 'Z': 2},
# {'Y': -43.9582085609436, 'X': -19.86978740492944, 'Z': 2}
# ]


def getWaypointsFromFile():
	base_path = "/var/www/"
	#Arquivo onde sao guardados os pontos de GPS calculados pelo JS do localhost
	dataInputsFile = open(base_path + "gpsDataPoints.txt", "r")
	waypoint_list = []

	#Ler as linhas do arquivo de datapoints e separa as coordenadas x e y
	for line in dataInputsFile:
		y = re.search(r'([-*]\d+.\d+),', line)
		x = re.search(r',([-*]\d+.\d+)', line)
		waypoint = {}
		waypoint['X'] = float(x.group(1))
		waypoint['Y'] = float(y.group(1))
		waypoint['Z'] = 2
		waypoint_list.append(waypoint)


	dataInputsFile.close()
	return waypoint_list

# Passa todos os pontos GPS calculados pelo JS para o formato waypointList = [{"X": xvalue, "Y": yvalue}]
waypointList = getWaypointsFromFile()

class Waypoint:
	def __init__(self, x=0.0, y=0.0, z=0.0, heading=0.0):
		
		self.wp_number	= 1 # always 1
		self.dummy_1 	= 0 # (don't care)
		self.dummy_2	= 0 # (don't care)
		self.properties	= WPPROP_ABSCOORDS + WPPROP_YAWENABLED
		# + WPPROP_YAWENABLED
		#+ WPPROP_AUTOMATICGOTO
		#self.properties	= WPPROP_AUTOMATICGOTO 
		#WPPROP_HEIGHTENABLED + 
		# Velocidade do quadrotor de 0 a 3m/s
		self.max_speed 	= WAYPOINT_VEL # 0-100%
		#Tempo que o Quadrotor fica no waypoint
		self.time 		= 500 # in 1/100th s
		self.pos_acc 	= 1500 # (2m) in mm, how close it can be to be 'at the waypoint'
		
		#Waypoint initialization
		self.X = 		int(x*(10**7)) # [mm]
		self.Y = 		int(y*(10**7)) # [mm]
		
			
		# self.height =	int(z*1000) # [mm]
		self.height = int(z) # [mm]
		############################
		if heading < MIN_YAW_REF:
			heading = MIN_YAW_REF
		if heading > MAX_YAW_REF:
			heading = MAX_YAW_REF

		self.yaw = 	int(heading*1000) # [deg*1000]
		############################
		self.chksum = 0
		############################
		self.chksum_short = 0

		
	#########################################################################
	# cria waypoint para mandar
	# number: 1..n
	# x, y, z: [m]
	# heading: [deg]
	#########################################################################
	def get_Waypoint(self):

		# calcula o checksum with absolute coordinates (lat and long)
		self.chksum = (0xaaaa+ self.yaw + self.height +self.time+self.X+self.Y+self.max_speed+self.pos_acc+self.properties+self.wp_number)
		#  Calculates cksum with
		# self.chksum = (0xAAAA+ self.yaw + 5000 +self.time+(self.X/(10**7))+(self.Y/(10**7))+self.max_speed+self.pos_acc+self.properties+self.wp_number)
		# delimita o checksum

		self.chksum = self.chksum % 32768

		#B = unsigned char, H = unsigned short, h = short, 4i = four int's g iiii)
		New_position = struct.Struct('BBHBBHHh4i')

		checksum = struct.Struct('h')
		checksum = checksum.pack(self.chksum)
		#print "unpack! ",struct.unpack('H', checksum);

		hexstring = binascii.hexlify(checksum)
		hexlist = [hexstring[i:i+2] for i in range(0,len(hexstring), 2)]
		hexlistreversed = list(reversed(hexlist))
		inthexreversed = ''.join(hexlistreversed)
		x = int(hexstring, 16)
		#print "chcksum :",hexstring, "int :", x, " hexlistreversed :", inthexreversed, 16
		self.chksum_short = struct.unpack('h', checksum)[0]
		#self.chksum_short = x


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
									self.height)		# i = int
										
	#########################################################################
	def show(self):	
		# print "x = " + str(self.X) + "\ty = " + str(self.Y) + "\tz = " + str(self.height) + "\tyaw = " + str(self.yaw)
		print "\nDENTRO DO publish_waypoint_by_index()"
		print "wp_number: ", self.wp_number
		print "dummy 1: ", self.dummy_1
		print "dummy 2: ", self.dummy_2
		print "properties: ", self.properties
		print "max_speed: ", self.max_speed
		print "time at waypoint: ", self.time
		print "position accuracy: ", self.pos_acc
		print "chksum: ", self.chksum_short
		print "X: ", self.X
		print "Y: ", self.Y
		print "yaw: ", self.yaw
		print "height: ", self.height

	def generateWPforROSPublish(self):	
		rosCommand = "'{wp_number: "+str(self.wp_number)+", dummy_1: 0, dummy_2: 0, properties: "+str(self.properties)+", max_speed: "+str(self.max_speed)+", time: "+str(self.time)+", pos_acc: "+str(self.pos_acc)+", chksum: "+str(self.chksum_short)+", X: "+str(self.X)+", Y: "+str(self.Y)+", yaw: "+str(self.yaw)+", height: "+str(int(self.zref))+"'}"
		return rosCommand

	def getValuesAsDict(self):
		return {'wp_number': self.wp_number, 'dummy_1': 0, 'dummy_2': 0, 'properties': self.properties, 'max_speed': self.max_speed, 'time': self.time, 'pos_acc': self.pos_acc, 'chksum': self.chksum_short, 'X': self.X, 'Y': self.Y, 'yaw': self.yaw, 'height': self.height}

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
		wp_data.height = self.height
		# self.show()		

		return wp_data
	#########################################################################

def gps_callback(data):
    global lat_val, lon_val, height_val, heading_val

    lat_val = float(data.latitude)/float(10**7)
    lon_val = float(data.longitude)/float(10**7)
    height_val = float(data.height)/1000.0
    heading_val = float(data.heading)/1000.0

    #print 'Lat: {0:+12.7f}'.format(lat_val)
    #print 'Lon: {0:+12.7f}'.format(lon_val)
    #print 'Height: {0: 7.3f}m'.format(height_val)
    #print 'Heading: {0: 7.3f}'.format(heading_val)

def ll_callback(data):
    global battery_val
    battery_val = float(data.battery_voltage_1)/1000.0
    #print 'Battery: {0:.3f}V'.format(battery_val)

def currentw_callback(data):
    global nav_status, distance_to_wp
    nav_status = int(data.navigation_status)
    distance_to_wp = float(data.distance_to_wp)*float(10)

    #print 'Nav status: '+str(nav_status)
    #print 'Distance to WP in CM: {0:.1f}'.format(distance_to_wp)


# def imuCalcData_callback(data):
# 	global height_val_imu, height_delta, roslaunch_height
# 	height_val_imu = int(data.height) #height after data fusion [mm]
# 	# height_val = int(data.height_reference) # height measured by the pressure sensor [mm]

# 	#Refere a diferenca de altura entre a altura atual do quadrotor fornecida pelo sensor IMU,
# 	# e a altura inicial de voo especificada.
# 	height_delta = height_val_imu - roslaunch_height #Not Used

# def gpsAdvanced_callback(data):
# 	global gps_numSV, gps_speedx, gps_speedy
# 	gps_numSV = int(data.numSV)
# 	# The bottom two are actually unsigned... Check to see how its done.
# 	gps_speedx = int(data.speed_x)
# 	gps_speedy = int(data.speed_y)



# def publish_next_waypoint(waypoint_cmd_publisher, waypoint_data_publisher):
    
#     print "PUBLISHING WAYPOINT"

#     wp_command = WaypointCommand()
#     wp_command.cmd = ">*>wg"
#     wp_command.header.stamp = rospy.get_rostime()
#     waypoint_cmd_publisher.publish(wp_command)

#     current_wp = waypointList.pop(0)
#     # wp = Waypoint(current_wp['X'], current_wp['Y'], current_wp['Z'], 0)
#     wp.get_Waypoint(0, 500)
#     #print wp.generateWPforROSPublish()
#     waypoint_data = wp.getWaypointStruct()
#     waypoint_data.header.stamp = rospy.get_rostime()
#     waypoint_data_publisher.publish(waypoint_data)

#     #print "WAYPOINT PUBLISHED",wp_command, waypoint_data
#     print "WAYPOINT PUBLISHED"

def publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index):
    global hummBaseName, roslaunch_height
    print "PUBLISHING WAYPOINT"

    #Before the command was set to send before the waypoint is ready. Was moved to here in the code.
    wp_command = WaypointCommand()
    wp_command.cmd = ">*>wg"
    wp_command.header.stamp = rospy.get_rostime()
    waypoint_cmd_publisher.publish(wp_command)



    current_wp = waypointList[waypoint_index]
    wp = Waypoint(current_wp['X'], current_wp['Y'], roslaunch_height, 0)
    wp.get_Waypoint() #usado para calcular chksum e parametros restantes nao inicializados
    #print wp.generateWPforROSPublish()
    waypoint_data = wp.getWaypointStruct()
    waypoint_data.header.stamp = rospy.get_rostime()
    waypoint_data_publisher.publish(waypoint_data)
    

    #print "WAYPOINT PUBLISHED",wp_command, waypoint_data
    print "WAYPOINT PUBLISHED"

def dist(lat1, lon1, lat2, lon2):
    #print lat1, lon1, lat2, lon2
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)

    lon2 = math.radians(lon2)
    x = (lon2-lon1) * math.cos((lat1+lat2)/2)
    y = (lat2-lat1)
    d = math.sqrt(x**2+y**2) * 6378137 #se quiser a distancia em mm multiplicar por 1000.
    return d * 100


def initialize_node():
    global nav_status, distance_to_wp, battery_val, lat_val, lon_val, height_val_imu, gps_speedy, gps_speedx, gps_numSV, hummBaseName, roslaunch_height
    
    rospy.init_node('waypoint_manager')
    if rospy.has_param('AutoPilotNodelet/hum'):
    	hummBaseName = rospy.get_param('AutoPilotNodelet/hum')
    if rospy.has_param('AutoPilotNodelet/height'):
    	roslaunch_height = rospy.get_param('AutoPilotNodelet/height')

    print "Hum, Height", hummBaseName, roslaunch_height

    
    rospy.Subscriber(hummBaseName + "/asctec/LL_STATUS", LLStatus, ll_callback)
    rospy.Subscriber(hummBaseName + "/asctec/GPS_DATA", GPSData, gps_callback)
    rospy.Subscriber(hummBaseName + "/asctec/CURRENT_WAY", CurrentWay, currentw_callback)
    # rospy.Subscriber(hummBaseName + "/asctec/GPS_DATA_ADVANCE", GPSDataAdvanced, gpsAdvanced_callback)
    # rospy.Subscriber(hummBaseName + "/asctec/IMU_CALCDATA", IMUCalcData, imuCalcData_callback)

    waypoint_cmd_publisher = rospy.Publisher(hummBaseName + '/asctec/WAYCOMMAND', WaypointCommand)
    waypoint_data_publisher = rospy.Publisher(hummBaseName + '/asctec/WAYPOINT', WaypointData)

    rospy.sleep(3)
    r = rospy.Rate(2)

    waypoint_index = 0
    publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)

    r.sleep()

    while not rospy.is_shutdown():
    	os.system('clear') # Clear the shell

        current_wp = waypointList[waypoint_index]
        distance_calculated = dist(lat_val, lon_val, current_wp['Y'], current_wp['X'])
        
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        print st
        print "Quadrotor:  ", hummBaseName
        print "Distance calculated in CM:", distance_calculated
        print "Distance generated by UAV:", distance_to_wp
        print "Navigation status        :", nav_status
        print "Battery values           :", battery_val
	        # print "Quadrotor speed_x (E/W)  :", gps_speedx
	        # print "Quadrotor speed_y (N/S)  :", gps_speedy
	        # print "Number of satelites      :", gps_numSV
        # print "Height (IMU)				:", height_val_imu
        print "Current waypoint Number  :", waypoint_index
        print "Current waypoint         :", current_wp['Y'], current_wp['X']

        # if(distance_to_wp <= min_distance_inside_waypoint):
        if (nav_status == 7):
            print "		** Distance inside waypoint reached!"
			
            if(waypoint_index >= len(waypointList)):
                print "		** No more waypoints to send!"
                print "		** Program terminated!"
                return 0
            else:
            	waypoint_index += 1
            	print "		** Publishing waypoint [",waypoint_index,"]" 
                publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)
                rospy.sleep(3)
        r.sleep()


if __name__ == "__main__":
    initialize_node()
    rospy.spin()