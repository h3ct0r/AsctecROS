#!/usr/bin/python

import re
import rospy

from asctec_msgs.msg import LLStatus
from asctec_msgs.msg import IMUCalcData
from asctec_msgs.msg import GPSData
from asctec_msgs.msg import CurrentWay

from asctec_msgs.msg import WaypointCommand
from asctec_msgs.msg import WaypointData

class Quadrotor:

	def __init__(self, VERBOSE=0):

		self.name = "/" + rospy.get_param("~quadName", "hum1") # Default Quadrotor name hum1
		self.height = rospy.get_param("~height", 8000) # DefaultDefault  height 8 m
		self.velocity = rospy.get_param("~velocity", 90) # Default velocity of the quadrotor - 90 porcent
		self.waypointFile = rospy.get_param("~mainWaypointFiles", "/var/www/gpsDataPoints.txt") # file with waypoints (from GPS) to control the quadrotor
		self.waypointTime = rospy.get_param("~waypointTime") # Sets time quadrotor will stay at waypoint
		self.externalBaseName = '/' + rospy.get_param("~externalBaseName") # /ext

		self.waypoint_cmd_publisher = rospy.Publisher(self.name + '/asctec/WAYCOMMAND', WaypointCommand)
		self.waypoint_data_publisher = rospy.Publisher(self.name + '/asctec/WAYPOINT', WaypointData)

		rospy.Subscriber(self.name + "/asctec/LL_STATUS", LLStatus, self.ll_callback)
		rospy.Subscriber(self.name + "/asctec/GPS_DATA", GPSData, self.gps_callback)
		rospy.Subscriber(self.name + "/asctec/CURRENT_WAY", CurrentWay, self.currentw_callback)
		rospy.Subscriber(self.name + "/asctec/IMU_CALCDATA", IMUCalcData, self.imuCalcData_callback)

		self.lat_val = 0
		self.lon_val = 0
		self.height_val = 5
		self.heading_val = 0
		self.gps_numSV = 0
		# speed in x (E/W) and y(N/S) in mm/s
		self.gps_speedx = 0
		self.gps_speedy = 0
		self.battery_val = 0
		self.distance_to_wp = 0

		self.nav_status = 0
		self.height_val_imu = 0

		self.VERBOSE = VERBOSE


	# This function get the /ext and the /hum*(from respective quadrotor) waypoints from main waypoint file and save in two separated list
	def getWaypointFromFile(self):
		if self.VERBOSE:
			print "getWaypointsFromFile() called"
			print 'Waypoint filename:', self.waypointFile

		dataInputsFile = open(self.waypointFile, "r")

		self.externalWaypointList = []
		self.waypointList = []

		# Read the lines of the file and separate the x and y coordinates
		# Saves the coordinates in their respective lists
		for line in dataInputsFile:
			y = re.search(r',([-*]\d+.\d+),', line)
			x = re.search(r',([-*]\d+.\d+)\n', line)
			
			fileBaseName = re.search(r'([\/]ext)', line)
			fileQuadrotorBaseName = re.search(r'([\/]hum\d)', line)
			
			waypoint = {}
			waypoint['X'] = float(x.group(1))
			waypoint['Y'] = float(y.group(1))
			waypoint['Z'] = 2 # Maybe we can try use the height from Quadrotor

			if(fileBaseName != None and fileBaseName.group(1) == self.externalBaseName): # Compare to /ext
				self.externalWaypointList.append(waypoint)
				if self.VERBOSE:
					print line
			elif(fileQuadrotorBaseName != None and fileQuadrotorBaseName.group(1) == self.name): # Compare to /hum*
				self.waypointList.append(waypoint)
				if self.VERBOSE:
					print line


		dataInputsFile.close()

		self.externalWaypointListSize = len(self.externalWaypointList)
		self.waypointListSize = len(self.waypointList)

		# Sets the current quads waypointList_size_param
		if rospy.has_param("~waypointListSize"):
			rospy.set_param("~waypointListSize", self.waypointListSize)

		if self.VERBOSE:
			print "getWaypointsFromFile() done"


	def gps_callback(self, data):
		self.lat_val = float(data.latitude)/float(10**7)
		self.lon_val = float(data.longitude)/float(10**7)
		self.height_val = float(data.height)/1000.0
		self.heading_val = float(data.heading)/1000.0
		self.gps_numSV = int(data.numSV)
		self.gps_speedx = int(data.speed_x)
		self.gps_speedy = int(data.speed_y)

	def ll_callback(self, data):
		self.battery_val = float(data.battery_voltage_1)/1000.0

	def currentw_callback(self, data):
		self.nav_status = int(data.navigation_status)
		self.distance_to_wp = float(data.distance_to_wp)*float(10)

	def imuCalcData_callback(self, data):
		self.height_val_imu = int(data.height) #height after data fusion [mm]
		# self.height_val = int(data.height_reference) # height measured by the pressure sensor [mm]

	def setHomeOrLaunchWaypoint(self):
		wp_command = WaypointCommand()
		wp_command.cmd = ">*>wl"
		wp_command.header.stamp = rospy.get_rostime()
		self.waypoint_cmd_publisher.publish(wp_command)

	def landQuadrotor(self):
		wp_command = WaypointCommand()
		wp_command.cmd = ">*>we"
		wp_command.header.stamp = rospy.get_rostime()
		self.waypoint_cmd_publisher.publish(wp_command)

	def comeHomeQuadrotor(self):
		wp_command = WaypointCommand()
		wp_command.cmd = ">*>wh"
		wp_command.header.stamp = rospy.get_rostime()
		self.waypoint_cmd_publisher.publish(wp_command)