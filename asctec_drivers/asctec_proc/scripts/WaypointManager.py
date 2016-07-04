#!/usr/bin/python

import roslib; roslib.load_manifest('asctec_mon')
import rospy

from WaypointTimes import WaypointTimes
from Quadrotor import Quadrotor

import os
import math
import json


class WaypointManager:
    def __init__(self, VERBOSE=0):
        self.VERBOSE = VERBOSE

        # Intialize ros node
        rospy.init_node('waypointManager')

        # file with waypoints (from GPS) to control the quadrotor
        self.waypointFile = rospy.get_param("~mainWaypointFiles",
                                            "/var/www/gpsDataPoints.txt")
        # Default Quadrotor name hum1
        self.name = "/" + rospy.get_param("~quadName", "hum1")

        # Default External Waypoint name /ext
        self.externalBaseName = '/' + rospy.get_param("~externalBaseName", "/ext")

        # Get the Waypoint list and externalWaypoint list from file
        self.currentWaypointIndex = 0
        self.currentHexagonIndex = 0

        #self.getWaypointFromFile()
        #self.getWaypointFromJson()
        self.managerStatus = 0

        # Initialize the callbacks and get parameters from Quadrotor
        self.quad = Quadrotor(self.VERBOSE)

    # Enable to plot a path that quadrotor has done
    def setPlotMapGpsOn(self, condition):
        plotMapOn = False
        if rospy.has_param("~plotMapOn"):
            plotMapOn = rospy.get_param("~plotMapOn")
        if plotMapOn != condition:
            rospy.set_param("~plotMapOn", condition)

    # Calcute the distance (m) between Waypoint
    def dist(self, lat1, lon1, lat2, lon2):
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)

        lon2 = math.radians(lon2)
        x = (lon2 - lon1) * math.cos((lat1 + lat2) / 2)
        y = (lat2 - lat1)
        d = math.sqrt(x ** 2 + y ** 2) * 6378137
        return d  # in meters

    '''
    def printStatus(self):
        print "\33[1;91m                              Waypoint Status                                   \33[0m"
        print "\33[1;91m________________________________________________________________________________\33[0m"
        print "Current Waypoint Index             :", self.currentWaypointIndex, " of ", self.waypointListSize - 1
        print "Distance calculated by manager     :", self.distance
        print "Current Waypoint                   :", self.currentWaypoint['lat'], self.currentWaypoint['lng']
        print "\33[1;91m________________________________________________________________________________\33[0m"
    '''

    # This function get the /ext and the /hum*(from respective quadrotor) waypoints from main waypoint file and save in two separated list
    def getWaypointFromFile(self):
        if self.VERBOSE:
            print "Loading Waypoints from ", self.waypointFile

        dataInputsFile = open(self.waypointFile, "r").read()
        dataInputsFile = dataInputsFile.split('\n')
        self.externalWaypointList = []
        self.hexagonList = []
        waypointList = []

        for line in dataInputsFile:
            line = line.split(',')
            if len(line) == 1:
                continue
            name = line[0]
            lat = float(line[1])
            lng = float(line[2])
            waypoint = {}
            waypoint['lat'] = float(lat)
            waypoint['lng'] = float(lng)
            if len(line) == 4:
                height = float(line[3])
                waypoint['height'] = float(height)
            else:
                waypoint['height'] = None

            if (name == self.externalBaseName):
                self.externalWaypointList.append()
            elif (name == self.name):
                waypointList.append(waypoint)

        self.externalWaypointListSize = len(self.externalWaypointList)
        self.waypointListSize = len(waypointList)
        self.hexagonList.append(waypointList)
        self.currentWaypointIndex = 0

        # Sets the current quads waypointList_size_param
        if rospy.has_param("~waypointListSize"):
            rospy.set_param("~waypointListSize", self.waypointListSize)
        if self.VERBOSE:
            print "A total of " + str(self.waypointListSize) + " Waypoints and " + str(
                self.externalWaypointListSize) + " external Waypoints was loaded.\n"


    # Get the waypoints from json file
    def getWaypointFromJson(self):
        # list of hexagons
        self.hexagonList = []

        # open json file
        with open(self.waypointFile) as data_file:
            data = json.load(data_file)

        # Check if there are waypoint for this especific quadrotor
        if not self.name[4] in data:
            return

        # Update data with especific datas to quadrotor
        hexagons = data[self.name[4]]

        # Number of waypoints
        self.waypointListSize = 0

        # Get the waypoint data structure for each hexagon
        for hexagon in hexagons:
            waypointList = []
            self.waypointListSize += len(hexagon)
            for point in hexagon:
                waypoint = {}
                waypoint['lat'] = float(point[0])
                waypoint['lng'] = float(point[1])
                waypoint['height'] = None
                if len(point) == 3:
                    waypoint['height'] = float(point[2])
                waypointList.append(waypoint)
            self.hexagonList.append(waypointList)

        # Sets the current quads waypointList_size_param
        if rospy.has_param("~waypointListSize"):
            rospy.set_param("~waypointListSize", self.waypointListSize)

        # Show Waypoint Size loaded
        if self.VERBOSE:
            print "A total of " + str(self.waypointListSize) + " Waypoints and " + str(len(hexagons)) +" Hexagons was readed.\n"


    # Need to be tested!!!
    def startWaypointListNavigation(self):
        if rospy.has_param("~finishedWaypoints"):
            rospy.set_param("~finishedWaypoints", False)

        self.currentWaypointIndex = 0
        self.currentHexagonIndex = 0

        # take the first waypoint from the first hexagon
        self.currentWaypoint = self.hexagonList[self.currentHexagonIndex][self.currentWaypointIndex]

        # Send command to go at this point
        self.quad.gotoWaypoint(self.currentWaypoint)

        timer = rospy.get_time()
        # While Start Waypoint or Autonomous Navigation
        while self.managerStatus is 2 or self.managerStatus is 6:
            # Send command again if quadrotor don't change it status
            if (rospy.get_time() - timer ) > 5.0 and self.quad.navStatus != 7 and self.quad.navStatus != 5:
                self.quad.gotoWaypoint(self.currentWaypoint)
                timer = rospy.get_time()

            # If it archive at the waypoint
            if self.quad.navStatus == 7  and self.quad.distanceToWp < 200:
                # Check if there are more waypoint
                if self.currentWaypointIndex >= (len(self.hexagonList[self.currentHexagonIndex]) - 1):
                    if self.currentHexagonIndex >= (len(self.hexagonList) - 1):
                        self.managerStatus = 9
                        return
                    else:
                        self.currentHexagonIndex += 1
                        self.currentWaypointIndex = 0
                else:
                    # take the next waypoint and send command to quadrotor
                    self.currentWaypointIndex += 1
                    self.currentWaypoint = self.hexagonList[self.currentHexagonIndex][self.currentWaypointIndex]
                    self.quad.gotoWaypoint(self.currentWaypoint)

                    # This ensures that the waypoints wont jump in the list
                    timer = rospy.get_time()
                    while self.quad.navStatus != 0:
                        if (rospy.get_time() - timer) > 2.0:
                            self.quad.gotoWaypoint(self.currentWaypoint)
                            timer = rospy.get_time()
                    timer = rospy.get_time()



        ''' --Without Hexagons--
        if rospy.has_param("~finishedWaypoints"):
            rospy.set_param("~finishedWaypoints", False)
        self.currentWaypointIndex = 0
        self.currentWaypoint = self.waypointList[self.currentWaypointIndex]
        self.quad.gotoWaypoint(self.currentWaypoint)
        timer = rospy.get_time()
        while self.managerStatus is 2 or self.managerStatus is 6:
            if (rospy.get_time() - timer > 5.0) and self.quad.navStatus != 7 and self.quad.navStatus != 5:
                self.quad.gotoWaypoint(self.currentWaypoint)
                timer = rospy.get_time()

            if self.quad.navStatus == 7 and self.quad.distanceToWp < 100:
                if self.currentWaypointIndex >= (self.waypointListSize - 1):
                    # if rospy.has_param("~finishedWaypoints"):
                    #    rospy.set_param("~finishedWaypoints", True)
                    self.managerStatus = 9
                    return
                else:
                    self.currentWaypointIndex += 1
                    self.currentWaypoint = self.waypointList[self.currentWaypointIndex]
                    self.quad.gotoWaypoint(self.currentWaypoint)

                    # This ensures that the waypoints wont jump in the list
                    timer = rospy.get_time()
                    while self.quad.navStatus != 0:
                        if (rospy.get_time() - timer) > 2.0:
                            self.quad.gotoWaypoint(self.currentWaypoint)
                            timer = rospy.get_time()
                    timer = rospy.get_time()
        '''

    # Must be improved - Don't use
    def autonomousNavigation(self):
        # Must be adjust with navigation status variable
        self.managerStatus = 1
        self.quad.launchQuadrotor()
        rospy.sleep(8)

        self.managerStatus = 5
        self.quad.setHomeWaypoint()
        rospy.sleep(2)

        self.managerStatus = 6
        self.startWaypointListNavigation()
        if self.managerStatus is not 9:
            return

        self.managerStatus = 3
        self.quad.comeHomeQuadrotor()
        while self.quad.navStatus is not 7:
            pass
        self.managerStatus = 0
        self.quad.landQuadrotor()

    # State Machine to control each behaviour of the quadrobot from interface
    def runUI(self):  # State Machine
        timer = rospy.get_time()
        filename = 'navStatus' + str(rospy.get_rostime()) + '.txt'
        f = open(filename, 'w')

        while not rospy.is_shutdown():
            if self.managerStatus is 0 and (rospy.get_time() - timer) > 5:  # Idle or Land State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.landQuadrotor()
                self.setPlotMapGpsOn(False)
                timer = rospy.get_time()
            elif self.managerStatus is 1 and (rospy.get_time() - timer) > 5:  # Launch State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.setPlotMapGpsOn(True)
                self.quad.launchQuadrotor()
                timer = rospy.get_time()
            elif self.managerStatus is 2:  # Autonomous Navigation State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.autonomousNavigation()
            elif self.managerStatus is 5 and (rospy.get_time() - timer) > 5:  # Set Home State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.setHomeWaypoint()
                timer = rospy.get_time()
            elif self.managerStatus is 6:  # Start Waypoint List State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.startWaypointListNavigation()
            elif self.managerStatus is 3 and (rospy.get_time() - timer) > 5:  # Come Home State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.comeHomeQuadrotor()
                timer = rospy.get_time()
        f.close()


if __name__ == "__main__":

    # Intialize the waypoint manager to control the quadrotors
    wm = WaypointManager(VERBOSE=1)
    try:
        wm.run()
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Waypoint Manager"
