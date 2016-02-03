#!/usr/bin/env python

import roslib; roslib.load_manifest('asctec_mon')
import rospy
import Queue
import random
import threading
import time
import re
import numpy as np
from time import sleep
from roslib import message
from collections import deque
from sensor_msgs.msg import Imu
import matplotlib.pyplot as plt
from random import randrange, uniform
import matplotlib.animation as animation

from asctec_msgs.msg import LLStatus
from asctec_msgs.msg import IMUCalcData
from asctec_msgs.msg import GPSData

counter = 0
dataList = []
plotMapOn = False
file_name = ""

#Usado para dar o nome do arquivo onde o mapa sera criado
ts = time.time();
ts = str(ts);
ts = re.search(r'(\d+)', ts)
# file_name = "/tmp/map" + ts.group(1) + ".html"    -- Commando ja executado abaixo, apenas ilustrativo.


class GraphData:
  '''
    Class to create an updated list for the graph
  '''
  def __init__(self, maxLen, rangeStart, rangeEnd):
      self.ax = ([0.0]*maxLen)
      self.maxLen = maxLen
      self.rangeStart = rangeStart
      self.rangeEnd = rangeEnd

  def addToBuf(self, buf, val):
      if len(buf) < self.maxLen:
          buf.append(val)
      else:
          buf.pop(0)
          buf.append(val)

  def appendValue(self, data):
      self.addToBuf(self.ax, data)

  def updateValue(self, data):
      try:
          # Change data for another value comming from ROS
          #data = random.randint(self.rangeStart,self.rangeEnd)
          self.appendValue(data)
      except KeyboardInterrupt:
          print('exiting')

      return self.ax

def updateGraph():
    global counter
    global dataList

    if(len(dataList) <= 0):
      #print "updateGraph: No data to show"
      win.after(10, updateGraph)
      return
    #else:
    #  print "updateGraph: DataList size:", len(dataList)

    data = dataList.pop()

    #print data

    counter += 1
    allX.pop(0)
    allX.append(counter)

    # plot Pitch
    line1.set_xdata(allX)
    line1.set_ydata(gPitch.updateValue(data.orientation.x))
    ax1.set_xlim(min(allX), max(allX))

    # plot Roll
    line2.set_xdata(allX)
    line2.set_ydata(gRoll.updateValue(data.orientation.y))
    ax2.set_xlim(min(allX), max(allX))

    # plot Yaw
    line3.set_xdata(allX)
    line3.set_ydata(gYaw.updateValue(data.orientation.z))
    ax3.set_xlim(min(allX), max(allX))

    fig.canvas.draw()
    plt.pause(0.0001)
    win.after(10, updateGraph)

def generateHTML():
    global dataList, file_name
    lastLat = str('{0:+12.7f}'.format(float(dataList[-1].latitude)/float(10**7)))
    lastLon = str('{0:+12.7f}'.format(float(dataList[-1].longitude)/float(10**7)))
    coordList = ""
    for data in dataList:
        coordList += "new google.maps.LatLng(" + str('{0:+12.7f}'.format(float(data.latitude)/float(10**7))) + "," + str('{0:+12.7f}'.format(float(data.longitude)/float(10**7))) + "),"
    output = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple Polylines</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
    <script>
// This example creates a 2-pixel-wide red polyline showing
// the path of William Kingsford Smith's first trans-Pacific flight between
// Oakland, CA, and Brisbane, Australia.

function initialize() {
  var mapOptions = {
    zoom: 20,
    center: new google.maps.LatLng(""" + lastLat + "," + lastLon + """),
    mapTypeId: google.maps.MapTypeId.SATELLITE
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var flightPlanCoordinates = [""" + coordList[:-1] + """
  ];
  var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  flightPath.setMap(map);

    var populationOptions = {
      strokeColor: '#FF00FF',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FFFFFF',
      fillOpacity: 0.35,
      map: map,
      center: new google.maps.LatLng(""" + lastLat + """,""" + lastLon + """),
      radius: 1
    };
    // Add the circle for this city to the map.
    cityCircle = new google.maps.Circle(populationOptions);

}

google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
""" 
    # humm = ""
    # if rospy.has_param('AutoPilotNodelet/hum'):
    #   humm =  rospy.get_param('AutoPilotNodelet/hum')
    
    # #Cria um nome do arquivo novo, diferente de todos os outros
    # file_name = "/var/www/GpsFlightMaps/" + ts.group(1) + humm
    
    # # Sends the file path + name to maintain consistency between time and map files.
    # rospy.set_param('AutoPilotNodelet/mapFileName', file_name)
    # # print file_name
    # file_name += ".html"

    text_file = open(file_name, "w")
    text_file.write(output)
    text_file.close()


def callback(data):
    '''
        Function to be called from ROS Subscriber
    '''
    global dataList, plotMapOn
    #print data.orientation.x
    #if len(dataList) > 99:
     # dataList.pop()

    full_param = rospy.search_param('WaypointManager/plotMapOn')  
    if rospy.has_param(full_param):
      plotMapOn = rospy.get_param(full_param)
    if plotMapOn:
      dataList.append(data)
      generateHTML()




def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.

    global file_name
   
    rospy.init_node('listener', anonymous=True)
    hummBaseName = ""

    full_param = rospy.search_param('WaypointManager/quadName')
    if rospy.has_param(full_param):
      hummBaseName = rospy.get_param(full_param)
    
    print "Quadrotor:  ", hummBaseName
    rospy.Subscriber("/" + hummBaseName + "/asctec/GPS_DATA", GPSData, callback)

    
    #Cria um nome do arquivo novo, diferente de todos os outros
    full_param = rospy.search_param('WaypointManager/mapFileDirectory')
    file_name = rospy.get_param(full_param) + ts.group(1) + hummBaseName

    
    # Sends the file path + name to maintain consistency between time and map files.
    full_param = rospy.search_param('WaypointManager/mapFileName')
    rospy.set_param(full_param, file_name)

    file_name = file_name + ".html"

if __name__ == '__main__':

    # xSize = 100 

    # #gPitch = GraphData(xSize, -90000, 90000)
    # #gRoll = GraphData(xSize, -90000, 90000)
    # #gYaw = GraphData(xSize, 0 ,360000)

    # gPitch = GraphData(xSize, -1.0, 1.0)
    # gRoll = GraphData(xSize, -1.0, 1.0)
    # gYaw = GraphData(xSize, -1.0, 1.0)

    # #plt.show(block=False)

    # gPitchY = []
    # gRollY = []
    # gYawY = []

    # allX = []
    # counter = xSize

    # for i in range(xSize):
    #     gPitchY.append(0)
    #     gRollY.append(0)
    #     gYawY.append(0)
    #     allX.append(i)

    # fig = plt.figure()

    # ax1 = fig.add_subplot(311)
    # line1, = ax1.plot([], [], 'r-') # Returns a tuple of line objects, thus the comma
    # #ax1.set_ylim([-90100, 90100])
    # ax1.set_ylim([-1.1, 1.1])
    # ax1.set_title('Pitch Graph')

    # ax2 = fig.add_subplot(312)
    # line2, = ax2.plot(allX, gRollY, 'r-') # Returns a tuple of line objects, thus the comma
    # #ax2.set_ylim([-90100, 90100])
    # ax2.set_ylim([-1.1, 1.1])
    # ax2.set_title('Roll Graph')

    # ax3 = fig.add_subplot(313)
    # line3, = ax3.plot(allX, gYawY, 'r-') # Returns a tuple of line objects, thus the comma
    # #ax3.set_ylim([-100, 360000])
    # ax3.set_ylim([-1.1, 1.1])
    # ax3.set_title('Yaw Graph')

    # fig.text(0.06, 0.5, '', ha='center', va='center', rotation='vertical')
    # fig.text(0.5, 0.04, 'Time steps', ha='center', va='center')

    # plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)

    try:
        print("Node starting.")
        listener()
        # win = fig.canvas.manager.window
        #win.after(10, updateGraph)
        #plt.show(block=True)
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Node finished.")

    '''
    for i in range(200):

        callback(
            (random.randint(gPitch.rangeStart,gPitch.rangeEnd),
                random.randint(gRoll.rangeStart,gRoll.rangeEnd),
                random.randint(gYaw.rangeStart,gYaw.rangeEnd)
            ))
  '''