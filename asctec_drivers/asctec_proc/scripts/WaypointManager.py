#!/usr/bin/python

import roslib; roslib.load_manifest('asctec_mon')
import rospy
import sys

from WaypointTimes import WaypointTimes
from Quadrotor import Quadrotor

import os
import math
import time
import datetime
import re
import math


class WaypointManager:

	def __init__(self, VERBOSE=0):
		self.VERBOSE = VERBOSE

		# Intialize ros node
		rospy.init_node('waypointManager')

		self.waypointFile = rospy.get_param("~mainWaypointFiles", "/var/www/gpsDataPoints.txt") # file with waypoints (from GPS) to control the quadrotor
		self.name = "/" + rospy.get_param("~quadName", "hum1") # Default Quadrotor name hum1
		self.externalBaseName = '/' + rospy.get_param("~externalBaseName") # /ext



	def setPlotMapGpsOn(self, condition):
		plotMapOn = False
		if rospy.has_param("~plotMapOn"):
			plotMapOn = rospy.get_param("~plotMapOn")
		if plotMapOn != condition:
			rospy.set_param("~plotMapOn", condition)



	# Calcute the distance (m) between Waypoint
	def dist(self, lat1, lon1, lat2, lon2):
		#print lat1, lon1, lat2, lon2
		lat1 = math.radians(lat1)
		lon1 = math.radians(lon1)
		lat2 = math.radians(lat2)

		lon2 = math.radians(lon2)
		x = (lon2-lon1) * math.cos((lat1+lat2)/2)
		y = (lat2-lat1)
		d = math.sqrt(x**2+y**2) * 6378137
		return d # in meters



	def printStatus(self):
		print "\33[1;91m                              Waypoint Status                                   \33[0m"
		print "\33[1;91m________________________________________________________________________________\33[0m"
		print "Current Waypoint Index             :", self.currentWaypointIndex, " of ", self.waypointListSize-1
		print "Current Waypoint                   :", self.currentWaypoint['Y'], self.currentWaypoint['X']
		print "Distance calculated by manager     :", self.distance
		print "\33[1;91m________________________________________________________________________________\33[0m"



	# This function get the /ext and the /hum*(from respective quadrotor) waypoints from main waypoint file and save in two separated list
	def getWaypointFromFile(self):
		if self.VERBOSE:
			print "Loading Waypoints from ", self.waypointFile

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
				
			elif(fileQuadrotorBaseName != None and fileQuadrotorBaseName.group(1) == self.name): # Compare to /hum*
				self.waypointList.append(waypoint)
				
		dataInputsFile.close()

		self.externalWaypointListSize = len(self.externalWaypointList)
		self.waypointListSize = len(self.waypointList)

		# Sets the current quads waypointList_size_param
		if rospy.has_param("~waypointListSize"):
			rospy.set_param("~waypointListSize", self.waypointListSize)

		if self.VERBOSE:
			print "A total of " + str(self.waypointListSize) + " Waypoints and " + str(self.externalWaypointListSize) + " external Waypoints was loaded.\n"



	# Initialize the Quadrotor and manages its route
	def run(self):
		# Initialize the callbacks and get parameters from Quadrotor
		quad = Quadrotor(self.VERBOSE)

		# Get the Waypoint list and externalWaypoint list from file
		self.getWaypointFromFile()

		# Setting for now to false
		quad.thisQuadisRunningExternalWaypoints = False

		# Init ros rate
		r = rospy.Rate(2)

		# Test to see if quadrotor launches
		raw_input("\33[1;91mLaunch quadrotor? \33[0m")
		print "Quadrotor is taking off!"
		quad.launchQuadrotor()

		# Time until quadrotor has finished taking off
		raw_input("\33[1;91mIs take off finished? (Set home waypoint)\33[0m")
		# Set home quadrotor
		quad.setHomeWaypoint()

		r.sleep()

		# Publish the first waypoint
		self.currentWaypointIndex = 0
		self.currentWaypoint = self.waypointList[self.currentWaypointIndex]
		self.distance = self.dist(quad.latitude, quad.longitude, self.currentWaypoint['Y'], self.currentWaypoint['X'])
		quad.gotoWaypoint(self.currentWaypoint)
		
		# Initiates plot_gps_data.py to start plotting map data
		self.setPlotMapGpsOn(True)

		r.sleep()

		# Keeps timestamp of waypoints sent and arrived at
		wt = WaypointTimes(self.VERBOSE)
		wt.printWaypointSent(self.currentWaypointIndex, self.currentWaypoint)

		while not rospy.is_shutdown():
			# Clear the shell
			os.system('clear')

			# Print informations about the status of Quadrotor
			quad.printStatus()
			self.printStatus()

			# if quadrotor is not aproximating than send waypoint again
			if self.dist(quad.latitude, quad.longitude, self.currentWaypoint['Y'], self.currentWaypoint['X']) >= self.distance and quad.navStatus != 7: 
				quad.gotoWaypoint(self.currentWaypoint)

			self.distance = self.dist(quad.latitude, quad.longitude, self.currentWaypoint['Y'], self.currentWaypoint['X'])

			if quad.navStatus == 7:
				# Quadrotor has arrieved at current waypoint
				wt.printArrivedAtWaypoint(self.currentWaypointIndex, self.currentWaypoint)

				if self.currentWaypointIndex >= (self.waypointListSize-1):
					# TODO: Manager the quadrotor to go to external waypoint
					# Check if other quadrotor has finish and go to external waypoints
					if rospy.has_param("~finishedWaypoints"):
						rospy.set_param("~finishedWaypoints", True)
						self.setPlotMapGpsOn(False)
						break

				else:
					self.currentWaypointIndex += 1
					self.currentWaypoint = self.waypointList[self.currentWaypointIndex]
					quad.gotoWaypoint(self.currentWaypoint)
					wt.printWaypointSent(self.currentWaypointIndex, self.currentWaypoint)

					# This ensures that the waypoints wont jump in the list
					# It muss will test if that really occur
					count = 0
					print "In nav_status == 7"
					while quad.navStatus == 7:
						count += 1
						if count == 100:
							quad.gotoWaypoint(self.currentWaypoint)
							count = 0


			r.sleep()

		rospy.sleep(1)

		print "\n\33[1;93mWaiting for the quadrotor to come to Home or First Waypoint position (4m proximity radius) before landing.\33[0m\n\n"

		raw_input("\33[1;91mCome quadrotor to home?\33[0m")
		quad.comeHomeQuadrotor()
		# As long as quadrotor is no instructed to Do nothing, land at current position
		raw_input("\33[1;91m\nLand quadrotor?\33[0m");
		quad.landQuadrotor()




if __name__ == "__main__":

 	# Intialize the waypoint manager to control the quadrotors
	wm = WaypointManager(VERBOSE=1)
	
	try:
		wm.run()
		rospy.spin()
	except KeyboardInterrupt:
		print "Shutting down ROS Waypoint Manager"