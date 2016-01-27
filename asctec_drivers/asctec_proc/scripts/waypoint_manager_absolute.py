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
import math
from AsctecConfigParser import ConfigParser



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

onFinishedLoadingWaypoints = False
hummBaseName = ""
roslaunch_height = 0
height_val_imu = 0
# speed in x (E/W) and y(N/S) in mm/s
gps_speedx = 0 
gps_speedy = 0
#Numero de satelites
gps_numSV = 0 


waypointList = []
externalWaypointList = []
waypointTime = 1

configs = ConfigParser("/opt/ros/groovy/share/asctec_drivers/asctec_proc/scripts/asctec_drivers_config.xml")


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
# waypointList = [{'X': -43.95809590816498, 'Y': -19.869439295357967, 'Z': 2},
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

#Figura Hexagono - Pontos no campo de futebol perto Antonio Carlos
# waypointList = [
# {'X': -43.960407972335815, 'Y': -19.860968393557826, 'Z': 2},
# {'X': -43.96025240421295, 'Y': -19.861054164336647, 'Z': 2},
# {'X': -43.960204124450684, 'Y': -19.861139935069094, 'Z': 2},
# {'X': -43.96051526069641, 'Y': -19.860968393557826, 'Z': 2},
# {'X': -43.96054208278655, 'Y': -19.861013801622978, 'Z': 2},
# {'X': -43.9602255821228, 'Y': -19.86118534308515, 'Z': 2},
# {'X': -43.96025240421295, 'Y': -19.861230751088193, 'Z': 2},
# {'X': -43.96057426929474, 'Y': -19.861054164336647, 'Z': 2},
# {'X': -43.96060109138489, 'Y': -19.861094527040045, 'Z': 2},
# {'X': -43.9602792263031, 'Y': -19.86127111374666, 'Z': 2},
# {'X': -43.96030604839325, 'Y': -19.861316521725147, 'Z': 2},
# {'X': -43.96062791347504, 'Y': -19.861139935069094, 'Z': 2},
# {'X': -43.96057963371277, 'Y': -19.861225705755157, 'Z': 2},
# {'X': -43.960413336753845, 'Y': -19.861316521725147, 'Z': 2},
# {'X': -43.96052062511444, 'Y': -19.861316521725147, 'Z': 2},
# {'X': -43.96011829376221, 'Y': -19.861235796421067, 'Z': 2}
# ]

#Figura quadrada - Pontos no campo de futebol perto Antonio Carlos
# waypointList = [{'X': -43.96051526069641, 'Y': -19.861054164336647, 'Z': 2},
# {'X': -43.96051526069641, 'Y': -19.861235796421067, 'Z': 2},
# {'X': -43.96032214164734, 'Y': -19.861235796421067, 'Z': 2},
# {'X': -43.96032214164734, 'Y': -19.861054164336647, 'Z': 2},
# {'X': -43.96051526069641, 'Y': -19.861054164336647, 'Z': 2},
# {'X': -43.96011829376221, 'Y': -19.861235796421067, 'Z': 2}
# ]



class WaypointTimes:

	def __init__(self, fileName):
		self.f = open(fileName, 'w+')

	def printWaypointSent(self, waypointIndex):
		text = "Waypoint " + str(waypointIndex) + " sent at: " + str(time.time()) + "\n"
		self.f.write(text)
		# print "Called with text : " + text, self.f

	def printArrivedAtWaypoint(self, waypointIndex):
		text = "Waypoint " + str(waypointIndex) + " arrived at: " + str(time.time()) + "\n"
		self.f.write(text)

	def __del__(self):
		self.f.close()

def getWaypointsFromFile(fileName):
	global hummBaseName, onFinishedLoadingWaypoints
	print "functionGetWaypointsFromFile called"
	# base_path = "/var/www/"
	#Arquivo onde sao guardados os pontos de GPS calculados pelo JS do localhost
	# dataInputsFile = open(base_path + "gpsDataPoints.txt", "r")
	dataInputsFile = open(fileName, "r")
	waypoint_list = []

	print "hummBaseName" + hummBaseName

	#Ler as linhas do arquivo de datapoints e separa as coordenadas x e y
	for line in dataInputsFile:
		y = re.search(r',([-*]\d+.\d+),', line)
		x = re.search(r',([-*]\d+.\d+)\n', line)

		fileQuadrotorBaseName = re.search(r'([\/]hum\d)', line)

		if fileQuadrotorBaseName != None:
			if(hummBaseName == fileQuadrotorBaseName.group(1)):
				# print "equality: " + hummBaseName + " == " + fileQuadrotorBaseName.group(1)
				# print hummBaseName == fileQuadrotorBaseName.group(1)
				waypoint = {}
				waypoint['X'] = float(x.group(1))
				waypoint['Y'] = float(y.group(1))
				waypoint['Z'] = 2
				waypoint_list.append(waypoint)

	dataInputsFile.close()
	onFinishedLoadingWaypoints = True
	return waypoint_list

def getExternalWaypointsFromFile(fileName):
	print "getExternalWaypointsFromFile() called"
	global externalWaypointList
	# base_path = "/var/www/"
	#Arquivo onde sao guardados os pontos de GPS calculados pelo JS do localhost
	# dataInputsFile = open(base_path + "gpsDataPoints.txt", "r")
	dataInputsFile = open(fileName, "r")
	waypoint_list = []

	#Ler as linhas do arquivo de datapoints e separa as coordenadas x e y
	for line in dataInputsFile:
		y = re.search(r',([-*]\d+.\d+),', line)
		x = re.search(r',([-*]\d+.\d+)\n', line)
		
		fileBaseName = re.search(r'([\/]ext)', line)
		if(fileBaseName != None):
			if(fileBaseName.group(1) == '/' + str(configs.external_base_name)):
				# print "equality: " + hummBaseName + " == " + fileQuadrotorBaseName.group(1)
				# print hummBaseName == fileQuadrotorBaseName.group(1)
				waypoint = {}
				waypoint['X'] = float(x.group(1))
				waypoint['Y'] = float(y.group(1))
				waypoint['Z'] = 2
				waypoint_list.append(waypoint)

	dataInputsFile.close()
	return waypoint_list

# print "getWaypointsFromFile"
# # Passa todos os pontos GPS calculados pelo JS para o formato waypointList = [{"X": xvalue, "Y": yvalue}]
# waypointList = getWaypointsFromFile()



class Waypoint:
	def __init__(self, x=0.0, y=0.0, z=0.0, heading=0.0):
		
		self.wp_number	= 1 # always 1
		self.dummy_1 	= 0 # (don't care)
		self.dummy_2	= 0 # (don't care)
		self.properties	= WPPROP_ABSCOORDS + WPPROP_YAWENABLED + WPPROP_HEIGHTENABLED
		# + WPPROP_YAWENABLED
		#+ WPPROP_AUTOMATICGOTO
		#self.properties	= WPPROP_AUTOMATICGOTO 
		#WPPROP_HEIGHTENABLED + 
		# Velocidade do quadrotor de 0 a 3m/s
		self.max_speed 	= WAYPOINT_VEL # 0-100%
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
	global configs
	plotMapOn = False
	if rospy.has_param(configs.plot_map_on_param):
		plotMapOn = rospy.get_param(configs.plot_map_on_param)
	if plotMapOn != condition:
		rospy.set_param(configs.plot_map_on_param, condition)

def initTimeKeeper():
	global configs
	if rospy.has_param(configs.map_file_name_param):
		print rospy.get_param(configs.map_file_name_param)
    	mapFileName = rospy.get_param(configs.map_file_name_param) + "TimeStamps.txt"
	wt = WaypointTimes(mapFileName)
	return wt



def waypointFileChooser():
	global configs
	answer = ""
	while answer != "y" and answer != "n":
		answer = raw_input("Would you like to continue from last waypoint? [y/n]  ")
		print answer, type(answer)

	if(answer == "n"):
		return configs.main_waypoint_files
	else:
		return configs.backup_waypoint_files



def updateBackupGpsPointsFile(waypoint_index, waypointList):
	global hummBaseName, configs
	
	newWaypointList = waypointList
	f = open(configs.backup_waypoint_files, "w")
	
	for waypoint in newWaypointList:
		f.write(hummBaseName + "," + str(waypoint["Y"]) + "," + str(waypoint["X"]) + "\n")
	
	f.close()



def setHomeOrLaunchWaypoint(waypoint_cmd_publisher):
	wp_command = WaypointCommand()
	wp_command.cmd = ">*>wl"
	wp_command.header.stamp = rospy.get_rostime()
	waypoint_cmd_publisher.publish(wp_command)



def chooseFinalAction(answer, waypoint_cmd_publisher, waypoint_data_publisher, savedHomeLatitude=0, savedHomeLongitude=0):
	global waypointList, roslaunch_height

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
def setWaypointStayTimes(hummBaseName, waypointListSize):
	global configs

	humm = re.search(r'((/[a-z]+)([0-9]+))', hummBaseName)
	
	waypointListSizeOtherQuad = 0
	if(humm != None):
		isOddQuadNumber = int(humm.group(3)) % 2
	
	# Assertion that makes sure that hummBaseName quad number exists
	if(humm != None and isOddQuadNumber):

		hummCurrentQuadNumber = int(humm.group(3))
		hummOtherQuadNumber = hummCurrentQuadNumber + 1
		hummBase = humm.group(2)
		hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"

		#Extracts the other quads waypointList size from param
		if rospy.has_param(hummBaseNameOtherQuad + configs.waypointList_size_param):
			waypointListSizeOtherQuad = rospy.get_param(hummBaseNameOtherQuad + str(configs.waypointList_size_param))

		print "hummBaseNameOtherQuad -  " + hummBaseNameOtherQuad  + ":  ", waypointListSizeOtherQuad

		# # The multiplier will only be applied to the quadrotor that has a larger number of waypoints
		if(waypointListSize >= waypointListSizeOtherQuad and waypointListSizeOtherQuad != 0):
			timeMultiplier = math.ceil( waypointListSize / float(waypointListSizeOtherQuad))
			print "Time multiplier: ", timeMultiplier

			#Current quads size is larger, multiply its waypoint time (timeMultiplier squared to compensate time it takes to check waypoint)
			if rospy.has_param(configs.waypoint_time_param):
				currentTime = rospy.get_param(str(configs.waypoint_time_param))
				rospy.set_param(str(configs.waypoint_time_param), int(timeMultiplier*timeMultiplier) * currentTime)

		elif (waypointListSize < waypointListSizeOtherQuad and waypointListSizeOtherQuad != 0):
			timeMultiplier = math.ceil( waypointListSizeOtherQuad / float(waypointListSize))
			print "Time multiplier: ", timeMultiplier

			# Other quads waypoint list is larger, multiply its waypoint time
			currentTime = rospy.get_param(hummBaseNameOtherQuad + str(configs.waypoint_time_param))
			rospy.set_param(hummBaseNameOtherQuad + str(configs.waypoint_time_param), int(timeMultiplier*timeMultiplier) * currentTime)

	print "\n\n"


def checkOtherQuadrotorFinishedStatus():
	global configs

	humm = re.search(r'((/[a-z]+)([0-9]+))', hummBaseName)
	
	waypointListSizeOtherQuad = 0
	if(humm != None):
		isOddQuadNumber = int(humm.group(3)) % 2
	
	# Assertion that makes sure that hummBaseName quad number exists and is odd, gets the next quadrotor.
	if(humm != None and isOddQuadNumber):
		hummCurrentQuadNumber = int(humm.group(3))
		hummOtherQuadNumber = hummCurrentQuadNumber + 1
		hummBase = humm.group(2)
		hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"

		#Extracts the other quads waypointList size from param
		if rospy.has_param(hummBaseNameOtherQuad + configs.finishedWaypoints):
			otherQuadIsFinished = rospy.get_param(hummBaseNameOtherQuad + str(configs.finishedWaypoints))

		print "hummBaseNameOtherQuad -  " + hummBaseNameOtherQuad  + ":  ", otherQuadIsFinished

		return otherQuadIsFinished

	# Assertion that makes sure that hummBaseName quad number exists and is odd, gets the previous quadrotor.
	elif (humm != None and not isOddQuadNumber):
		hummCurrentQuadNumber = int(humm.group(3))
		hummOtherQuadNumber = hummCurrentQuadNumber - 1
		hummBase = humm.group(2)
		hummBaseNameOtherQuad = hummBase + str(hummOtherQuadNumber) + "/"

		#Extracts the other quads waypointList size from param
		if rospy.has_param(hummBaseNameOtherQuad + configs.finishedWaypoints):
			otherQuadIsFinished = rospy.get_param(hummBaseNameOtherQuad + str(configs.finishedWaypoints))

		print "hummBaseNameOtherQuad -  " + hummBaseNameOtherQuad  + ":  ", otherQuadIsFinished

		return otherQuadIsFinished

	print "\n\n"



####################################################

def initialize_node():
	global nav_status, distance_to_wp, battery_val, lat_val, lon_val, height_val_imu, gps_speedy, gps_speedx, gps_numSV, hummBaseName, roslaunch_height, waypointList, WAYPOINT_VEL
	global onFinishedLoadingWaypoints, configs, waypointTime, externalWaypointList

	rospy.init_node('waypoint_manager')
	if rospy.has_param(str(configs.hummingbird_name_param)):
		hummBaseName = "/" + rospy.get_param(str(configs.hummingbird_name_param))
	if rospy.has_param(configs.hummingbird_height_param):
		roslaunch_height = rospy.get_param(str(configs.hummingbird_height_param))
	if rospy.has_param(str(configs.hummingbird_velocity_param)):
		WAYPOINT_VEL = rospy.get_param(str(configs.hummingbird_velocity_param))


	# Need to fix how the backup file chooser updates
	# file_name = ""
	# file_name = waypointFileChooser()

	#Hardcoded for now
	file_name = configs.main_waypoint_files


	thisQuadisRunningExternalWaypoints = False

	# Gets the extra external waypoints
	externalWaypointList = getExternalWaypointsFromFile(file_name)

	#If points aren't being loaded from file onFinishedLoadingWaypoints = True, else False
	waypointList = getWaypointsFromFile(file_name)


	#Backup in case hardcoded points are being read, instead of from file.
	onFinishedLoadingWaypoints = True


	# Sets the current quads waypointList_size_param
	if rospy.has_param(str(configs.waypointList_size_param)):
			rospy.set_param(str(configs.waypointList_size_param), len(waypointList))
	rospy.sleep(2)
	# Used to configure the respective waypoint times for the pair of quadrotors
	setWaypointStayTimes(hummBaseName, len(waypointList))

	# Sets time quadrotor will stay at waypoint
	if rospy.has_param(str(configs.waypoint_time_param)):
		waypointTime = rospy.get_param(str(configs.waypoint_time_param))

	# print "Current Quad Waypoint Time: ", waypointTime


	print "waypointList size: " + str(len(waypointList))
	print "Hum, Height, Velocity", hummBaseName, roslaunch_height, WAYPOINT_VEL

	
	if (onFinishedLoadingWaypoints == True):
		rospy.Subscriber(hummBaseName + "/asctec/LL_STATUS", LLStatus, ll_callback)
		rospy.Subscriber(hummBaseName + "/asctec/GPS_DATA", GPSData, gps_callback)
		rospy.Subscriber(hummBaseName + "/asctec/CURRENT_WAY", CurrentWay, currentw_callback)
		rospy.Subscriber(hummBaseName + "/asctec/IMU_CALCDATA", IMUCalcData, imuCalcData_callback)

		waypoint_cmd_publisher = rospy.Publisher(hummBaseName + '/asctec/WAYCOMMAND', WaypointCommand)
		waypoint_data_publisher = rospy.Publisher(hummBaseName + '/asctec/WAYPOINT', WaypointData)

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
	firstWaypoint = waypointList[0]

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
	wt = initTimeKeeper()
	wt.printWaypointSent(waypoint_index)



	while not rospy.is_shutdown():
		

		os.system('clear') # Clear the shell

		current_wp = waypointList[waypoint_index]
		distance_calculated = dist(lat_val, lon_val, current_wp['Y'], current_wp['X'])

		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		print st
		print "Quadrotor:  ", hummBaseName
		print "Distance calculated in m:", distance_calculated
		print "Distance generated by UAV:", distance_to_wp
		print "Navigation status        :", nav_status
		print "Battery values           :", battery_val
		# print "Quadrotor speed_x (E/W)  :", gps_speedx
		# print "Quadrotor speed_y (N/S)  :", gps_speedy
		print "Number of satelites      :", gps_numSV
		print "Height (IMU)             :", height_val_imu, "m"
		print "Waypoint Velocity        :", WAYPOINT_VEL, "%"
		print "Waypoint List Size       :", str(len(waypointList))
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

			if(waypoint_index >= len(waypointList)-1):
				# print "		** No more waypoints to send!"
				# print "		** Program terminated!"
				# Set the quadrotor to finished main waypoints
				if rospy.has_param(str(configs.finishedWaypoints)):
					rospy.set_param(str(configs.finishedWaypoints), True)

				otherQuadIsFinished = checkOtherQuadrotorFinishedStatus()

				if not otherQuadIsFinished and not thisQuadisRunningExternalWaypoints:
					thisQuadisRunningExternalWaypoints = True
					waypointList = externalWaypointList
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