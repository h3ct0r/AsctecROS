#!/usr/bin/env python

import roslib; roslib.load_manifest('asctec_mon')
import rospy
import datetime
import os

from asctec_msgs.msg import GPSData


class PlotGPSData:
  def __init__(self):

    # Init ROS
    rospy.init_node('PlotGpsData', anonymous=True)

    self.dataList = []

    self.hummBaseName = self.getQuadName()
    
    print "Quadrotor:  ", self.hummBaseName
    # GPS callback event
    rospy.Subscriber("/" + self.hummBaseName + "/asctec/GPS_DATA", GPSData, self.gpsCallback)

    # Get the file name to save the datas
    self.fileName = self.getMapFileName()
    
    # Sends the file path + name to maintain consistency between time and map files.
    # Used to save the waypoint timestamp
    fullParam = rospy.search_param('WaypointManager/mapFileName')
    rospy.set_param(fullParam, self.fileName)

    
  def getQuadName(self):
    fullParam = rospy.search_param('WaypointManager/quadName')
    if rospy.has_param(fullParam):
      hummBaseName = rospy.get_param(fullParam) 
    else:
      hummBaseName = ""
    return hummBaseName


  def getMapFileName(self):
    # Get time structure
    dt = datetime.datetime.now()

    # Get the diretory where the file will be saved
    fullParam = rospy.search_param('WaypointManager/mapFileDirectory')
    path = rospy.get_param(fullParam) + dt.strftime("%Y-%m-%d")

    # Create a folder if it not exist year-month-day
    try: 
      os.makedirs(path)
    except OSError:
      pass

    # /hour_min_sec_hum*
    fileName = path + "/" + dt.strftime("%H_%M_%S_") + self.hummBaseName
    return fileName
    

  def getPlotMapOnStatus(self):
    fullParam = rospy.search_param('WaypointManager/plotMapOn')
    if rospy.has_param(fullParam):
      plotMapOn = rospy.get_param(fullParam)
    else:
      plotMapOn = False
    return plotMapOn


  def gpsCallback(self, data):
    plotMapOn = self.getPlotMapOnStatus()

    # Generate online a html file
    if plotMapOn:
      self.dataList.append(data)
      self.generateHTML()


  def generateHTML(self):
    lastLat = str('{0:+12.7f}'.format(float(self.dataList[-1].latitude)/float(10**7)))
    lastLon = str('{0:+12.7f}'.format(float(self.dataList[-1].longitude)/float(10**7)))
    coordList = ""
    for data in self.dataList:
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
    textFile = open(self.fileName + ".html", "w")
    textFile.write(output)
    textFile.close()




if __name__ == '__main__':
  try:
    print("PlotGPSData starting.")
    plot = PlotGPSData()      
    rospy.spin()
  except rospy.ROSInterruptException:
    print("Node finished.")