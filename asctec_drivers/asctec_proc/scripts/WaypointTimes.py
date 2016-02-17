#!/usr/bin/python

import rospy
import time

class WaypointTimes:

	def __init__(self, VERBOSE=0):
		fileName = rospy.get_param("~mapFileName", "/tmp/TimeStamps.txt")
		self.f = open(fileName, 'w+')  		
		if VERBOSE:
			print "Saving timestamp at ", fileName
		

	def printWaypointSent(self, waypointIndex, waypoint):
		text = "Waypoint " + str(waypointIndex) + " (" + str(waypoint['Y']) + ", " + str(waypoint['X']) + ") sent at: " + str(time.time()) + "\n"
		self.f.write(text)
		# print "Called with text : " + text, self.f

	def printArrivedAtWaypoint(self, waypointIndex, waypoint):
		text = "Waypoint " + str(waypointIndex) + " (" + str(waypoint['Y']) + ", " + str(waypoint['X']) + ") arrived at: " + str(time.time()) + "\n"
		self.f.write(text)

	def __del__(self):
		self.f.close()
