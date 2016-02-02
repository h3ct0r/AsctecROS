#!/usr/bin/python

import rospy
import time

class WaypointTimes:

	def __init__(self):
		print rospy.has_param("~mapFileName")
		fileName = rospy.get_param("~mapFileName", "TimeStamps.txt")
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
