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

from WaypointTimes import WaypointTimes
from Quadrotor import Quadrotor

import struct
import binascii
import os
import math
import time
import datetime
import re
import math

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

onFinishedLoadingWaypoints = False
height_val_imu = 0
# speed in x (E/W) and y(N/S) in mm/s
gps_speedx = 0 
gps_speedy = 0
#Numero de satelites
gps_numSV = 0 

quad = None # Class Quadrotor
waypointTime = 1

VERBOSE = 1


class Waypoint:
	def __init__(self, x=0.0, y=0.0, z=0.0, heading=0.0, velocity=50):
		
		self.wp_number	= 1 # always 1
		self.dummy_1 	= 0 # (don't care)
		self.dummy_2	= 0 # (don't care)
		self.properties	= WPPROP_ABSCOORDS + WPPROP_YAWENABLED + WPPROP_HEIGHTENABLED
		# + WPPROP_YAWENABLED
		#+ WPPROP_AUTOMATICGOTO
		#self.properties	= WPPROP_AUTOMATICGOTO 
		#WPPROP_HEIGHTENABLED + 
		# Velocidade do quadrotor de 0 a 3m/s
		self.max_speed 	= velocity # 0-100%
		#Tempo que o Quadrotor fica no waypoint
		self.time 		= waypointTime * 100 # in 1/100th s
		self.pos_acc 	= 2000 # (2m) in mm, how close it can be to be 'at the waypoint'
		
		#Waypoint initialization
		# X is Longitude, Y is Latitude
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
#	def show(self):	
#		# print "x = " + str(self.X) + "\ty = " + str(self.Y) + "\tz = " + str(self.height) + "\tyaw = " + str(self.yaw)
#		print "\nDENTRO DO publish_waypoint_by_index()"
#		print "wp_number: ", self.wp_number
#		print "dummy 1: ", self.dummy_1
#		print "dummy 2: ", self.dummy_2
#		print "properties: ", self.properties
#		print "max_speed: ", self.max_speed
#		print "time at waypoint: ", self.time
#		print "position accuracy: ", self.pos_acc
#		print "chksum: ", self.chksum_short
#		print "X: ", self.X
#		print "Y: ", self.Y
#		print "yaw: ", self.yaw
#		print "height: ", self.height

	#def generateWPforROSPublish(self):	
	#	rosCommand = "'{wp_number: "+str(self.wp_number)+", dummy_1: 0, dummy_2: 0, properties: "+str(self.properties)+", max_speed: "+str(self.max_speed)+", time: "+str(self.time)+", pos_acc: "+str(self.pos_acc)+", chksum: "+str(self.chksum_short)+", X: "+str(self.X)+", Y: "+str(self.Y)+", yaw: "+str(self.yaw)+", height: "+str(int(self.zref))+"'}"
	#	return rosCommand

	#def getValuesAsDict(self):
	#	return {'wp_number': self.wp_number, 'dummy_1': 0, 'dummy_2': 0, 'properties': self.properties, 'max_speed': self.max_speed, 'time': self.time, 'pos_acc': self.pos_acc, 'chksum': self.chksum_short, 'X': self.X, 'Y': self.Y, 'yaw': self.yaw, 'height': self.height}

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
    global lat_val, lon_val, height_val, heading_val, gps_numSV, gps_speedx, gps_speedy

    lat_val = float(data.latitude)/float(10**7)
    lon_val = float(data.longitude)/float(10**7)
    height_val = float(data.height)/1000.0
    heading_val = float(data.heading)/1000.0
    gps_numSV = int(data.numSV)
    gps_speedx = int(data.speed_x)
    gps_speedy = int(data.speed_y)

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


def imuCalcData_callback(data):
    global height_val_imu
    height_val_imu = int(data.height) #height after data fusion [mm]
    # height_val = int(data.height_reference) # height measured by the pressure sensor [mm]

def publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index):
    global quad
    print "PUBLISHING WAYPOINT"

    #Before the command was set to send before the waypoint is ready. Was moved to here in the code.
    wp_command = WaypointCommand()
    wp_command.cmd = ">*>wg"
    wp_command.header.stamp = rospy.get_rostime()
    waypoint_cmd_publisher.publish(wp_command)

    current_wp = quad.waypointList[waypoint_index]
    wp = Waypoint(current_wp['X'], current_wp['Y'], quad.height, 0, quad.velocity)
    wp.get_Waypoint() #usado para calcular chksum e parametros restantes nao inicializados
    waypoint_data = wp.getWaypointStruct()
    waypoint_data.header.stamp = rospy.get_rostime()
    waypoint_data_publisher.publish(waypoint_data)
    
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
    return d # in meters



def setPlotMapGpsOn(condition):
	plotMapOn = False
	if rospy.has_param("~plotMapOn"):
		plotMapOn = rospy.get_param("~plotMapOn")
	if plotMapOn != condition:
		rospy.set_param("~plotMapOn", condition)


#def waypointFileChooser():
#	answer = ""
#	while answer != "y" and answer != "n":
#		answer = raw_input("Would you like to continue from last waypoint? [y/n]  ")
#		print answer, type(answer)
#
#	if(answer == "n"):
#		return rospy.get_param("~mainWaypointFiles")
#	else:
#		return rospy.get_param("~backupWaypointFiles")



def updateBackupGpsPointsFile(waypoint_index, waypointList):
	global quad
	
	newWaypointList = waypointList
	backupWaypointFiles = ""
	if rospy.has_param("~backupWaypointFiles"):
		backupWaypointFiles = rospy.get_param("~backupWaypointFiles")
	f = open(backupWaypointFiles, "w")
	
	for waypoint in newWaypointList:
		f.write(quad.name + "," + str(waypoint["Y"]) + "," + str(waypoint["X"]) + "\n")
	
	f.close()



def setHomeOrLaunchWaypoint(waypoint_cmd_publisher):
	wp_command = WaypointCommand()
	wp_command.cmd = ">*>wl"
	wp_command.header.stamp = rospy.get_rostime()
	waypoint_cmd_publisher.publish(wp_command)



def chooseFinalAction(answer, waypoint_cmd_publisher, waypoint_data_publisher, savedHomeLatitude=0, savedHomeLongitude=0):
	global quad

	if(answer == 1):
		print "		** No more waypoints to send!"
		print "		** Program terminated!"

	elif (answer == 2):
		publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, 0)
		print "Quadrotor going to first waypoint!"

	else:
		#Before the command was set to send before the waypoint is ready. Was moved to here in the code.
		print "Quadrotor returning to previously set Home Waypoint"
		comeHomeQuadrotor(waypoint_cmd_publisher)

		raw_input("Land quadrotor?")
		landQuadrotor(waypoint_cmd_publisher)




def landQuadrotor(waypoint_cmd_publisher):
	wp_command = WaypointCommand()
	wp_command.cmd = ">*>we"
	wp_command.header.stamp = rospy.get_rostime()
	waypoint_cmd_publisher.publish(wp_command)

def comeHomeQuadrotor(waypoint_cmd_publisher):
	wp_command = WaypointCommand()
	wp_command.cmd = ">*>wh"
	wp_command.header.stamp = rospy.get_rostime()
	waypoint_cmd_publisher.publish(wp_command)

###################################################
def setWaypointStayTimes(waypointListSize):
	global quad
	humm = re.search(r'((/[a-z]+)([0-9]+))', quad.name)
	
	waypointListSizeOtherQuad = 0
	if(humm != None):
		isOddQuadNumber = int(humm.group(3)) % 2
	
	# Assertion that makes sure that quad.name quad number exists
	if(humm != None and isOddQuadNumber):

		hummCurrentQuadNumber = int(humm.group(3))
		hummOtherQuadNumber = hummCurrentQuadNumber + 1
		hummBase = humm.group(2)
		hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"


		#Extracts the other quads waypointList size from param
		if rospy.has_param(hummBaseNameOtherQuad + "WaypointManager/waypointListSize"):
			waypointListSizeOtherQuad = rospy.get_param(hummBaseNameOtherQuad + "WaypointManager/waypointListSize")

		print "hummBaseNameOtherQuad -  " + hummBaseNameOtherQuad  + ":  ", waypointListSizeOtherQuad

		# # The multiplier will only be applied to the quadrotor that has a larger number of waypoints
		if(waypointListSize >= waypointListSizeOtherQuad and waypointListSizeOtherQuad != 0):
			timeMultiplier = math.ceil( waypointListSize / float(waypointListSizeOtherQuad))
			print "Time multiplier: ", timeMultiplier

			#Current quads size is larger, multiply its waypoint time (timeMultiplier squared to compensate time it takes to check waypoint)
			if rospy.has_param("~waypointTime"):
				currentTime = rospy.get_param("~waypointTime")
				rospy.set_param("~waypointTime", int(timeMultiplier*timeMultiplier) * currentTime)

		elif (waypointListSize < waypointListSizeOtherQuad and waypointListSizeOtherQuad != 0):
			timeMultiplier = math.ceil( waypointListSizeOtherQuad / float(waypointListSize))
			print "Time multiplier: ", timeMultiplier

			# Other quads waypoint list is larger, multiply its waypoint time
			currentTime = rospy.get_param(hummBaseNameOtherQuad + "WaypointManager/waypointTime")
			rospy.set_param(hummBaseNameOtherQuad + "WaypointManager/waypointTime", int(timeMultiplier*timeMultiplier) * currentTime)

	print "\n\n"


def checkOtherQuadrotorFinishedStatus():
	global quad
	humm = re.search(r'((/[a-z]+)([0-9]+))', quad.name)
	
	waypointListSizeOtherQuad = 0
	if(humm != None):
		isOddQuadNumber = int(humm.group(3)) % 2
	
	# Assertion that makes sure that quad.name quad number exists and is odd, gets the next quadrotor.
	if(humm != None and isOddQuadNumber):
		hummCurrentQuadNumber = int(humm.group(3))
		hummOtherQuadNumber = hummCurrentQuadNumber + 1
		hummBase = humm.group(2)
		hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"

		#Extracts the other quads waypointList size from param
		if rospy.has_param(hummBaseNameOtherQuad + "WaypointManager/finishedWaypoints"):
			otherQuadIsFinished = rospy.get_param(hummBaseNameOtherQuad + "WaypointManager/finishedWaypoints")

		print "hummBaseNameOtherQuad -  " + hummBaseNameOtherQuad  + ":  ", otherQuadIsFinished

		return otherQuadIsFinished

	# Assertion that makes sure that quad.name quad number exists and is odd, gets the previous quadrotor.
	elif (humm != None and not isOddQuadNumber):
		hummCurrentQuadNumber = int(humm.group(3))
		hummOtherQuadNumber = hummCurrentQuadNumber - 1
		hummBase = humm.group(2)
		hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"

		#Extracts the other quads waypointList size from param
		if rospy.has_param(hummBaseNameOtherQuad + "WaypointManager/finishedWaypoints"):
			otherQuadIsFinished = rospy.get_param(hummBaseNameOtherQuad + "WaypointManager/finishedWaypoints")

		print "hummBaseNameOtherQuad -  " + hummBaseNameOtherQuad  + ":  ", otherQuadIsFinished

		return otherQuadIsFinished

	print "\n\n"



####################################################

def initialize_node():
	global nav_status, distance_to_wp, battery_val, lat_val, lon_val, height_val_imu, gps_speedy, gps_speedx, gps_numSV
	global onFinishedLoadingWaypoints, waypointTime

	global quad

	rospy.init_node('waypoint_manager')

	quad = Quadrotor(VERBOSE=1)

	# Need to fix how the backup file chooser updates
	# file_name = ""
	# file_name = waypointFileChooser() # (rezeck) I dont not what that mean

	quad.getWaypointFromFile(VERBOSE=1) # Get the externalWaypoint list and the wapoints list from file

	thisQuadisRunningExternalWaypoints = False

	#Backup in case hardcoded points are being read, instead of from file.
	onFinishedLoadingWaypoints = True

	rospy.sleep(2)

	# Used to configure the respective waypoint times for the pair of quadrotors
	setWaypointStayTimes(quad.waypointListSize)

	# Sets time quadrotor will stay at waypoint
	if rospy.has_param("~waypointTime"):
		waypointTime = rospy.get_param("~waypointTime")

	# print "Current Quad Waypoint Time: ", waypointTime


	print "waypointList size: " + str(quad.waypointListSize)
	print "Hum, Height, Velocity", quad.name, quad.height, quad.velocity

	
	if (onFinishedLoadingWaypoints == True):
		rospy.Subscriber(quad.name + "/asctec/LL_STATUS", LLStatus, ll_callback)
		rospy.Subscriber(quad.name + "/asctec/GPS_DATA", GPSData, gps_callback)
		rospy.Subscriber(quad.name + "/asctec/CURRENT_WAY", CurrentWay, currentw_callback)
		rospy.Subscriber(quad.name + "/asctec/IMU_CALCDATA", IMUCalcData, imuCalcData_callback)

		waypoint_cmd_publisher = rospy.Publisher(quad.name + '/asctec/WAYCOMMAND', WaypointCommand)
		waypoint_data_publisher = rospy.Publisher(quad.name + '/asctec/WAYPOINT', WaypointData)

	# rospy.sleep(3)
	r = rospy.Rate(2)


	# Test to see if quadrotor launches
	raw_input("Launch quadrotor? ")
	print "Quadrotor is taking off!"
	setHomeOrLaunchWaypoint(waypoint_cmd_publisher)
	
	# Time until quadrotor has finished taking off
	
	raw_input("Is take off finished? (Set home waypoint)")
	# # Set home quadrotor
	setHomeOrLaunchWaypoint(waypoint_cmd_publisher)
	

	os.system('clear')

	savedHomeLatitude = lat_val
	savedHomeLongitude = lon_val
	firstWaypoint = quad.waypointList[0]

	#The default setting is do nothing homeAnswer=1
	homeAnswer = 3
	# if(dist(savedHomeLatitude, savedHomeLongitude, firstWaypoint['Y'], firstWaypoint['X']) < 100):
	# 	homeAnswer = int(raw_input("Would you like to:\n\t[1] Do Nothing\n\t[2] Go Back to First Waypoint of List\n\t[3] Set Home Waypoint\n\nAnswer:  "))

	print "savedHomeLatitude: ", savedHomeLatitude
	print "savedHomeLongitude: ", savedHomeLongitude
	print "firstWaypointLatitude: ", firstWaypoint['Y']
	print "firstWaypointLongitude: ", firstWaypoint['X']
	print "\n*** DISTANCE CALCULATED *** : ", dist(savedHomeLatitude, savedHomeLongitude, firstWaypoint['Y'], firstWaypoint['X'])

	rospy.sleep(4)

	# Publish the first waypoint
	waypoint_index = 0
	publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)

	# Initiates plot_gps_data.py to start plotting map data
	setPlotMapGpsOn(True)

	r.sleep()

	# Counter used to periodically send waypoint to Quadrotor, as backup
	counterToSendWaypointAgain = 0

	# Class that keeps timestamps of waypoints sent and arrived at.
	wt = WaypointTimes()
	wt.printWaypointSent(waypoint_index)



	while not rospy.is_shutdown():
		

		os.system('clear') # Clear the shell

		current_wp = quad.waypointList[waypoint_index]
		distance_calculated = dist(lat_val, lon_val, current_wp['Y'], current_wp['X'])

		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		print st
		print "Quadrotor:  ", quad.name
		print "Distance calculated in m:", distance_calculated
		print "Distance generated by UAV:", distance_to_wp
		print "Navigation status        :", nav_status
		print "Battery values           :", battery_val
		# print "Quadrotor speed_x (E/W)  :", gps_speedx
		# print "Quadrotor speed_y (N/S)  :", gps_speedy
		print "Number of satelites      :", gps_numSV
		print "Height (IMU)             :", height_val_imu, "m"
		print "Waypoint Velocity        :", quad.velocity, "%"
		print "Waypoint List Size       :", str(quad.waypointListSize)
		print "Current waypoint Number  :", waypoint_index
		print "Current waypoint (Y, X)  :", current_wp['Y'], current_wp['X']


		# Backup in case the quadrotor stops for some reason, or we have to move it.
		counterToSendWaypointAgain += 1
		if(counterToSendWaypointAgain == 20 and nav_status != 7):
			publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)
			counterToSendWaypointAgain = 0


		# if(distance_to_wp <= min_distance_inside_waypoint):
		# When waypoint is reached
		if (nav_status == 7):
			print "		** Distance inside waypoint reached!"
			wt.printArrivedAtWaypoint(waypoint_index)

			if(waypoint_index >= quad.waypointListSize-1):
				# print "		** No more waypoints to send!"
				# print "		** Program terminated!"
				# Set the quadrotor to finished main waypoints
				if rospy.has_param("~finishedWaypoints"):
					rospy.set_param("~finishedWaypoints", True)

				otherQuadIsFinished = checkOtherQuadrotorFinishedStatus()

				if not otherQuadIsFinished and not thisQuadisRunningExternalWaypoints:
					thisQuadisRunningExternalWaypoints = True
					quad.waypointListSize = quad.externalWaypointList
					waypoint_index = 0
					thisQuadisRunningExternalWaypoints = True

				else:
					setPlotMapGpsOn(False)
					chooseFinalAction(homeAnswer, waypoint_cmd_publisher, waypoint_data_publisher, savedHomeLatitude, savedHomeLongitude)
					return 0
			else:
				waypoint_index += 1
				print "		** Publishing waypoint [",waypoint_index,"]" 
				publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)
				# This ensures that the waypoints wont jump in the list
				count = 0
				while nav_status == 7:
					count = count + 1
					print "In nav_status == 7"
					rospy.sleep(1)
					if count == 10:
						publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)
					
				# publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)
				wt.printWaypointSent(waypoint_index)
		r.sleep()


	# In case the user wishes to continue from last waypoint
	# ****** To fix later ******

	# print "\n\nUpdating backup waypoints file, Quadrotor on Manual control"
	# updateBackupGpsPointsFile(waypoint_index, waypointList)
	
	# print "Lands quadrotor at current position"
	rospy.sleep(1)

	print "\nWaiting for the quadrotor to come to Home or First Waypoint position (4m proximity radius) before landing."
	
	print dist(savedHomeLatitude, savedHomeLongitude, lat_val, lon_val)


	### PUT all the information below inside the repeating loop! ###
	# while(dist(savedHomeLatitude, savedHomeLongitude, lat_val, lon_val) > 4) and (homeAnswer == 3):
	# 	print dist(savedHomeLatitude, savedHomeLongitude, lat_val, lon_val)

	# while(dist(firstWaypoint['Y'], firstWaypoint['X'], lat_val, lon_val) > 4) and (homeAnswer == 2):
	# 	pass


	# As long as quadrotor is no instructed to Do nothing, land at current position
	raw_input("Land quadrotor?");
	landQuadrotor(waypoint_cmd_publisher)

if __name__ == "__main__":
	initialize_node()
	rospy.spin()