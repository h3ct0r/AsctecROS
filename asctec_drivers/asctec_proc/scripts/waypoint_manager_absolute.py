#!/usr/bin/python

import roslib; roslib.load_manifest('asctec_mon')
import rospy
import sys

from WaypointTimes import WaypointTimes
from Quadrotor import Quadrotor
from Waypoint import Waypoint

from asctec_msgs.msg import WaypointCommand

import os
import math
import time
import datetime
import re
import math

min_distance_inside_waypoint = 50

onFinishedLoadingWaypoints = False

quad = None # Class Quadrotor

VERBOSE = 1


def publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index):
    global quad
    print "PUBLISHING WAYPOINT"

    #Before the command was set to send before the waypoint is ready. Was moved to here in the code.
    wp_command = WaypointCommand()
    wp_command.cmd = ">*>wg"
    wp_command.header.stamp = rospy.get_rostime()
    waypoint_cmd_publisher.publish(wp_command)

    current_wp = quad.waypointList[waypoint_index]
    wp = Waypoint(current_wp['X'], current_wp['Y'], quad.height, 0, quad.velocity, quad.waypointTime)
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
		quad.comeHomeQuadrotor()

		raw_input("Land quadrotor?")
		quad.landQuadrotor()

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
	global onFinishedLoadingWaypoints

	global quad

	rospy.init_node('waypoint_manager')

	quad = Quadrotor(VERBOSE=1)

	# Need to fix how the backup file chooser updates
	# file_name = ""
	# file_name = waypointFileChooser()

	quad.getWaypointFromFile() # Get the externalWaypoint list and the wapoints list from file

	thisQuadisRunningExternalWaypoints = False

	#Backup in case hardcoded points are being read, instead of from file.
	onFinishedLoadingWaypoints = True

	rospy.sleep(2)

	# Used to configure the respective waypoint times for the pair of quadrotors
	setWaypointStayTimes(quad.waypointListSize)

	print "waypointList size: " + str(quad.waypointListSize)
	print "Hum, Height, Velocity", quad.name, quad.height, quad.velocity

	# rospy.sleep(3)
	r = rospy.Rate(2)


	# Test to see if quadrotor launches
	raw_input("Launch quadrotor? ")
	print "Quadrotor is taking off!"
	quad.setHomeOrLaunchWaypoint()
	
	# Time until quadrotor has finished taking off
	
	raw_input("Is take off finished? (Set home waypoint)")
	# # Set home quadrotor
	quad.setHomeOrLaunchWaypoint()
	

	os.system('clear')

	savedHomeLatitude = quad.lat_val
	savedHomeLongitude = quad.lon_val
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
	publish_waypoint_by_index(quad.waypoint_cmd_publisher, quad.waypoint_data_publisher, waypoint_index)

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
		distance_calculated = dist(quad.lat_val, quad.lon_val, current_wp['Y'], current_wp['X'])

		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		print st
		print "Quadrotor:  ", quad.name
		print "Distance calculated in m:", distance_calculated
		print "Distance generated by UAV:", quad.distance_to_wp
		print "Navigation status        :", quad.nav_status
		print "Battery values           :", quad.battery_val
		# print "Quadrotor speed_x (E/W)  :", quad.gps_speedx
		# print "Quadrotor speed_y (N/S)  :", quad.gps_speedy
		print "Number of satelites      :", quad.gps_numSV
		print "Height (IMU)             :", quad.height_val_imu, "m"
		print "Waypoint Velocity        :", quad.velocity, "%"
		print "Waypoint List Size       :", str(quad.waypointListSize)
		print "Current waypoint Number  :", waypoint_index
		print "Current waypoint (Y, X)  :", current_wp['Y'], current_wp['X']


		# Backup in case the quadrotor stops for some reason, or we have to move it.
		counterToSendWaypointAgain += 1
		if(counterToSendWaypointAgain == 20 and quad.nav_status != 7):
			publish_waypoint_by_index(quad.waypoint_cmd_publisher, quad.waypoint_data_publisher, waypoint_index)
			counterToSendWaypointAgain = 0


		# if(quad.distance_to_wp <= min_distance_inside_waypoint):
		# When waypoint is reached
		if (quad.nav_status == 7):
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
					chooseFinalAction(homeAnswer, quad.waypoint_cmd_publisher, quad.waypoint_data_publisher, savedHomeLatitude, savedHomeLongitude)
					return 0
			else:
				waypoint_index += 1
				print "		** Publishing waypoint [",waypoint_index,"]" 
				publish_waypoint_by_index(quad.waypoint_cmd_publisher, quad.waypoint_data_publisher, waypoint_index)
				# This ensures that the waypoints wont jump in the list
				count = 0
				while quad.nav_status == 7:
					count = count + 1
					print "In nav_status == 7"
					rospy.sleep(1)
					if count == 10:
						publish_waypoint_by_index(quas.waypoint_cmd_publisher, quad.waypoint_data_publisher, waypoint_index)
					
				# publish_waypoint_by_index(quad.waypoint_cmd_publisher, quad.waypoint_data_publisher, waypoint_index)
				wt.printWaypointSent(waypoint_index)
		r.sleep()


	# In case the user wishes to continue from last waypoint
	# ****** To fix later ******

	# print "\n\nUpdating backup waypoints file, Quadrotor on Manual control"
	# updateBackupGpsPointsFile(waypoint_index, waypointList)
	
	# print "Lands quadrotor at current position"
	rospy.sleep(1)

	print "\nWaiting for the quadrotor to come to Home or First Waypoint position (4m proximity radius) before landing."
	
	print dist(savedHomeLatitude, savedHomeLongitude, quad.lat_val, quad.lon_val)


	### PUT all the information below inside the repeating loop! ###
	# while(dist(savedHomeLatitude, savedHomeLongitude, quad.lat_val, quad.lon_val) > 4) and (homeAnswer == 3):
	# 	print dist(savedHomeLatitude, savedHomeLongitude, quad.lat_val, quad.lon_val)

	# while(dist(firstWaypoint['Y'], firstWaypoint['X'], quad.lat_val, quad.lon_val) > 4) and (homeAnswer == 2):
	# 	pass


	# As long as quadrotor is no instructed to Do nothing, land at current position
	raw_input("Land quadrotor?");
	quad.landQuadrotor()

if __name__ == "__main__":
	initialize_node()
	rospy.spin()