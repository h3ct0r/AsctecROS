#!/usr/bin/python

import re
import rospy

class Quadrotor:

	def __init__(self, VERBOSE=0):

		self.name = "/" + rospy.get_param("~quadName", "hum1") # Default Quadrotor name hum1
		self.height = rospy.get_param("~height", 8000) # DefaultDefault  height 8 m
		self.velocity = rospy.get_param("~velocity", 90) # Default velocity of the quadrotor - 90 porcent
		self.waypointFile = rospy.get_param("~mainWaypointFiles", "/var/www/gpsDataPoints.txt") # file with waypoints (from GPS) to control the quadrotor
		self.externalBaseName = '/' + rospy.get_param("~externalBaseName") # /ext




	# This function get the /ext and the /hum*(from respective quadrotor) waypoints from main waypoint file and save in two separated list
	def getWaypointFromFile(self, VERBOSE=0):
		if VERBOSE:
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
				if VERBOSE:
					print line
			elif(fileQuadrotorBaseName != None and fileQuadrotorBaseName.group(1) == self.name): # Compare to /hum*
				self.waypointList.append(waypoint)
				if VERBOSE:
					print line


		dataInputsFile.close()

		self.externalWaypointListSize = len(self.externalWaypointList)
		self.waypointListSize = len(self.waypointList)

		# Sets the current quads waypointList_size_param
		if rospy.has_param("~waypointListSize"):
			rospy.set_param("~waypointListSize", self.waypointListSize)

		if VERBOSE:
			print "getWaypointsFromFile() done"