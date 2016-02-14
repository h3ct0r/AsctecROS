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


	def setPlotMapGpsOn(self, condition):
		plotMapOn = False
		if rospy.has_param("~plotMapOn"):
			plotMapOn = rospy.get_param("~plotMapOn")
		if plotMapOn != condition:
			rospy.set_param("~plotMapOn", condition)


	# Initialize the Quadrotor and manages its route
	def run(self):
		# Initialize the callbacks and get parameters from Quadrotor
		quad = Quadrotor(self.VERBOSE)

		# Get the Waypoint list and externalWaypoint list from file
		quad.getWaypointFromFile()

		# Setting for now to false
		quad.thisQuadisRunningExternalWaypoints = False

		# Sync time
		rospy.sleep(2)

		# Init ros rate
		r = rospy.Rate(2)

		# Test to see if quadrotor launches
		raw_input("Launch quadrotor? ")
		print "Quadrotor is taking off!"
		quad.launchQuadrotor()

		# Time until quadrotor has finished taking off
		raw_input("Is take off finished? (Set home waypoint)")
		# Set home quadrotor
		quad.setHomeWaypoint()

		# Publish the first waypoint
		quad.currentWaypointIndex = 0
		distance = quad.distanceToWp
		quad.gotoWaypoint(quad.currentWaypointIndex)
		
		# Initiates plot_gps_data.py to start plotting map data
		self.setPlotMapGpsOn(True)

		r.sleep()

		# Keeps timestamp of waypoints sent and arrived at
		wt = WaypointTimes(self.VERBOSE)
		wt.printWaypointSent(quad.currentWaypointIndex)

		while not rospy.is_shutdown():
			# Clear the shell
			os.system('clear')

			# Print informations about the status of Quadrotor
			quad.printStatus()

			# if quadrotor is not aproximating than send waypoint again
			if quad.currentDistanceCalculated >= distance and quad.navStatus != 7: 
				quad.gotoWaypoint(quad.currentWaypointIndex)

			distance = quad.currentDistanceCalculated

			if quad.navStatus == 7:
				# Quadrotor has arrieved at current waypoint
				wt.printArrivedAtWaypoint(waypointIndex)

				if quad.currentWaypointIndex >= (quad.waypointListSize-1):
					# TODO: Manager the quadrotor to go to external waypoint
					# Check if other quadrotor has finish and go to external waypoints
					if rospy.has_param("~finishedWaypoints"):
						rospy.set_param("~finishedWaypoints", True)
						self.setPlotMapGpsOn(False)
						break

				else:
					quad.currentWaypointIndex += 1
					quad.gotoWaypoint(quad.currentWaypointIndex)
					wt.printWaypointSent(quad.currentWaypointIndex)

					# This ensures that the waypoints wont jump in the list
					# It muss will test if that oc
					count = 0
					while quad.navStatus == 7:
						count += 1
						print "In nav_status == 7"
						rospy.sleep(1)
						if count == 10:
							quad.gotoWaypoint(quad.currentWaypointIndex)


			r.sleep()

		rospy.sleep(1)

		print "\nWaiting for the quadrotor to come to Home or First Waypoint position (4m proximity radius) before landing."
		
		#print dist(self., savedHomeLongitude, quad.latitude, quad.longitude)

		# As long as quadrotor is no instructed to Do nothing, land at current position
		raw_input("Land quadrotor?");
		quad.landQuadrotor()








if __name__ == "__main__":

 	# Intialize the waypoint manager to control the quadrotors
	wm = WaypointManager(VERBOSE=1)
	
	try:
		wm.run()
		rospy.spin()
	except KeyboardInterrupt:
		print "Shutting down ROS Waypoint Manager"