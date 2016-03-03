#!/usr/bin/python

import roslib; roslib.load_manifest('asctec_mon')
import rospy

from WaypointTimes import WaypointTimes
from Quadrotor import Quadrotor

import os
import math


class WaypointManager:
    def __init__(self, VERBOSE=0):
        self.VERBOSE = VERBOSE

        # Intialize ros node
        rospy.init_node('waypointManager')

        self.waypointFile = rospy.get_param("~mainWaypointFiles", "/var/www/gpsDataPoints.txt") # file with waypoints (from GPS) to control the quadrotor
        self.name = "/" + rospy.get_param("~quadName", "hum1") # Default Quadrotor name hum1
        self.externalBaseName = '/' + rospy.get_param("~externalBaseName") # /ext

        # Get the Waypoint list and externalWaypoint list from file
        self.getWaypointFromFile()
        self.managerStatus = 0

        # Initialize the callbacks and get parameters from Quadrotor
        self.quad = Quadrotor(self.VERBOSE)

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
        x = (lon2-lon1) * math.cos((lat1+lat2)/2)
        y = (lat2-lat1)
        d = math.sqrt(x**2+y**2) * 6378137
        return d # in meters

    def printStatus(self):
        print "\33[1;91m                              Waypoint Status                                   \33[0m"
        print "\33[1;91m________________________________________________________________________________\33[0m"
        print "Current Waypoint Index             :", self.currentWaypointIndex, " of ", self.waypointListSize-1
        print "Distance calculated by manager     :", self.distance
        print "Current Waypoint                   :", self.currentWaypoint['lat'], self.currentWaypoint['lng']
        print "\33[1;91m________________________________________________________________________________\33[0m"

    # This function get the /ext and the /hum*(from respective quadrotor) waypoints from main waypoint file and save in two separated list
    def getWaypointFromFile(self):
        if self.VERBOSE:
            print "Loading Waypoints from ", self.waypointFile

        dataInputsFile = open(self.waypointFile, "r").read()
        dataInputsFile = dataInputsFile.split('\n')
        self.externalWaypointList = []
        self.waypointList = []

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
                self.waypointList.append(waypoint)

        self.externalWaypointListSize = len(self.externalWaypointList)
        self.waypointListSize = len(self.waypointList)
        self.currentWaypointIndex = 0

        # Sets the current quads waypointList_size_param
        if rospy.has_param("~waypointListSize"):
            rospy.set_param("~waypointListSize", self.waypointListSize)
        if self.VERBOSE:
            print "A total of " + str(self.waypointListSize) + " Waypoints and " + str(self.externalWaypointListSize) + " external Waypoints was loaded.\n"


    def startWaypointListNavigation(self):
        if rospy.has_param("~finishedWaypoints"):
            rospy.set_param("~finishedWaypoints", False)
        self.currentWaypointIndex = 0
        self.currentWaypoint = self.waypointList[self.currentWaypointIndex]
        self.quad.gotoWaypoint(self.currentWaypoint)
        timer = rospy.get_time()
        while self.managerStatus is 2 or self.managerStatus is 6:
            if (rospy.get_time()- timer > 5.0) and self.quad.navStatus != 7 and self.quad.navStatus != 5:
                self.quad.gotoWaypoint(self.currentWaypoint)
                timer = rospy.get_time()

            if self.quad.navStatus == 7 and self.quad.distanceToWp < 100:
                if self.currentWaypointIndex >= (self.waypointListSize-1):
                    #if rospy.has_param("~finishedWaypoints"):
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


    def runUI(self): # State Machine
        timer = rospy.get_time()
        filename = 'navStatus' + str(rospy.get_rostime()) + '.txt'
        f = open(filename, 'w')

        while not rospy.is_shutdown():
            if self.managerStatus is 0 and (rospy.get_time()-timer) > 5:  # Idle or Land State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.landQuadrotor()
                timer = rospy.get_time()
            elif self.managerStatus is 1 and (rospy.get_time()-timer) > 5:  # Launch State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.launchQuadrotor()
                timer = rospy.get_time()
            elif self.managerStatus is 2:  # Autonomous Navigation State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.autonomousNavigation()
            elif self.managerStatus is 5 and (rospy.get_time()-timer) > 5:  # Set Home State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.setHomeWaypoint()
                timer = rospy.get_time()
            elif self.managerStatus is 6:  # Start Waypoint List State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.startWaypointListNavigation()
            elif self.managerStatus is 3 and (rospy.get_time()-timer) > 5:  # Come Home State
                f.write(str(self.quad.navStatus) + ',' + str(self.managerStatus) + '\n')
                self.quad.comeHomeQuadrotor()
                timer = rospy.get_time()
        f.close()

    # Initialize the Quadrotor and manages its route
    def run(self):
        if (self.waypointListSize == 0):
            print "There are no Waypoint to Quadrotor ", self.quad.name
            return

        # Setting for now to false
        self.quad.thisQuadisRunningExternalWaypoints = False

        # Init ros rate
        r = rospy.Rate(2)

        # Test to see if quadrotor launches
        raw_input("\33[1;91mLaunch quadrotor? \33[0m")
        print "Quadrotor is taking off!"
        self.quad.launchQuadrotor()

        # Time until quadrotor has finished taking off
        raw_input("\33[1;91mIs take off finished? (Set home waypoint)\33[0m")
        # Set home quadrotor
        self.quad.setHomeWaypoint()

        r.sleep()

        # Publish the first waypoint
        self.currentWaypointIndex = 0
        self.currentWaypoint = self.waypointList[self.currentWaypointIndex]
        self.distance = self.dist(self.quad.latitude, self.quad.longitude, self.currentWaypoint['lat'], self.currentWaypoint['lng'])
        self.quad.gotoWaypoint(self.currentWaypoint)

        # Initiates plot_gps_data.py to start plotting map data
        self.setPlotMapGpsOn(True)

        r.sleep()

        # Keeps timestamp of waypoints sent and arrived at
        wt = WaypointTimes(self.VERBOSE)
        wt.printWaypointSent(self.currentWaypointIndex, self.currentWaypoint)

        timer = rospy.get_time()

        while not rospy.is_shutdown():
            # Clear the shell
            os.system('clear')

            # Print informations about the status of Quadrotor
            self.quad.printStatus()
            self.printStatus()

            # if quadrotor is not aproximating than send waypoint again
            #if self.dist(quad.latitude, quad.longitude, self.currentWaypoint['lat'], self.currentWaypoint['lng']) >= self.distance and quad.navStatus != 7 and self.nav_status != 5:
            #	quad.gotoWaypoint(self.currentWaypoint)

            #self.distance = self.dist(quad.latitude, quad.longitude, self.currentWaypoint['lat'], self.currentWaypoint['lng'])

            if (rospy.get_time()- timer > 5.0) and self.quad.navStatus != 7 and self.quad.navStatus != 5:
                self.quad.gotoWaypoint(self.currentWaypoint)
                timer = rospy.get_time()

            if self.quad.navStatus == 7 and self.quad.distanceToWp < 200:
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
                    self.quad.gotoWaypoint(self.currentWaypoint)
                    wt.printWaypointSent(self.currentWaypointIndex, self.currentWaypoint)

                    # This ensures that the waypoints wont jump in the list
                    timer = rospy.get_time()

                    print "In navStatus ", self.quad.navStatus
                    while self.quad.navStatus != 0:
                        if (rospy.get_time() - timer) > 2.0:
                            self.quad.gotoWaypoint(self.currentWaypoint)
                            timer = rospy.get_time()

                    timer = rospy.get_time()

            rospy.sleep(1)

        rospy.sleep(1)

        print "\n\33[1;93mWaiting for the quadrotor to come to Home before landing.\33[0m\n"

        raw_input("\33[1;91mCome quadrotor to home?\33[0m")
        self.quad.comeHomeQuadrotor()
        # As long as quadrotor is no instructed to Do nothing, land at current position
        raw_input("\33[1;91m\nLand quadrotor?\33[0m");
        self.quad.landQuadrotor()

        while (self.quad.navStatus != 15):
            pass

        print "\33[1;92m\nMission completed!\33[0m"




if __name__ == "__main__":

    # Intialize the waypoint manager to control the quadrotors
    wm = WaypointManager(VERBOSE=1)
    try:
        wm.run()
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Waypoint Manager"