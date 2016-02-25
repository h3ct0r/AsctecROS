#!/usr/bin/python
import roslib; roslib.load_manifest('asctec_mon')
import sys
import rospy

from PyQt4 import QtCore, QtGui
from manui import Ui_MainWindow
from mapsScript import html

from WaypointManager import WaypointManager


class MyThread(QtCore.QThread):
  def __init__(self, ui, wm, parent=None):
      super(MyThread, self).__init__(parent)
      self.ui = ui
      self.wm = wm

  def run(self):
    try:
      self.wm.run()
      rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Waypoint Manager"


class ManUi(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ManUi, self).__init__(parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.ui.webView.setHtml(html)
    self.ui.webView.loadFinished.connect(self.loadFinished)

    self.wm = WaypointManager(VERBOSE=1)

    self.thread = MyThread(self.ui, self.wm)
    self.thread.start()
    # Wait to loop ros get some variables
    rospy.sleep(3)

    self.stimer = QtCore.QTimer()

    self.timer = QtCore.QTimer()
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.loop)

  def loadFinished(self):
      self.stimer.singleShot(100, self.setup)
      self.timer.start(200)

      self.ui.flightPathCheckbox.clicked.connect(self.flightPathCheckboxEvent)
      self.ui.quadrotorCheckbox.clicked.connect(self.quadrotorCheckboxEvent)
      self.ui.waypointCheckbox.clicked.connect(self.waypointCheckboxEvent)

  def flightPathCheckboxEvent(self):
      if self.ui.flightPathCheckbox.isChecked() is True:
          self.ui.webView.page().mainFrame().evaluateJavaScript("showFlighPath({0});".format(1))
      else:
          self.ui.webView.page().mainFrame().evaluateJavaScript("showFlighPath({0});".format(0))


  def quadrotorCheckboxEvent(self):
      if self.ui.quadrotorCheckbox.isChecked() is True:
          self.ui.webView.page().mainFrame().evaluateJavaScript("showMarkerPos({0});".format(1))
      else:
          self.ui.webView.page().mainFrame().evaluateJavaScript("showMarkerPos({0});".format(0))

  def waypointCheckboxEvent(self):
      if self.ui.waypointCheckbox.isChecked() is True:
          self.ui.webView.page().mainFrame().evaluateJavaScript("showWaypoints({0});".format(1))
      else:
          self.ui.webView.page().mainFrame().evaluateJavaScript("showWaypoints({0});".format(0))


  def setup(self):
    try:
      self.ui.quadNameText.setText(self.thread.wm.quad.name)
      self.ui.webView.page().mainFrame().evaluateJavaScript("initWaypointMarker({0});".format(self.thread.wm.waypointListSize))
      self.ui.heightSlider.setValue(self.thread.wm.quad.height)
      self.ui.velocitySlider.setValue(self.thread.wm.quad.velocity)

      #self.thread.wm.quad.latitude = -19.8695912 # apagar depois de ativar o gps
      #self.thread.wm.quad.longitude = -43.9583309
    except RuntimeWarning():
      pass

  def loop(self):
    try:
      self.ui.batteryBar.setValue(self.thread.wm.quad.batteryPercent)
      self.ui.navigationStatusText.setText(str(self.thread.wm.quad.navStatus))
      self.ui.batteryText.setText(str(self.thread.wm.quad.battery))

      self.thread.wm.quad.height = self.ui.heightSlider.value()
      self.thread.wm.quad.velocity = self.ui.velocitySlider.value()

      currentWaypointIndex = self.thread.wm.currentWaypointIndex
      self.ui.waypointIndexText.setText(str(currentWaypointIndex+1) + " of " + str(self.thread.wm.waypointListSize))
      self.ui.waypointDistanceText.setText(str(self.thread.wm.quad.distanceToWp))
      self.ui.waypointLatitudeText.setText(str(self.thread.wm.waypointList[currentWaypointIndex]['Y']))
      self.ui.waypointLongitudeText.setText(str(self.thread.wm.waypointList[currentWaypointIndex]['X']))
      self.ui.waypointHeightText.setText(str(self.thread.wm.quad.height))
      self.ui.waypointVelocityText.setText(str(self.thread.wm.quad.velocity))

      self.ui.gpsSatelitesText.setText(str(self.thread.wm.quad.gpsNumSV))
      self.ui.gpsLatitudeText.setText(str(self.thread.wm.quad.latitude))
      self.ui.gpsLongitudeText.setText(str(self.thread.wm.quad.longitude))
      self.ui.gpsAltitudeText.setText(str(self.thread.wm.quad.altitude))
      self.ui.gpsHeadingText.setText(str(self.thread.wm.quad.heading))
      self.ui.gpsImuHeightText.setText(str(self.thread.wm.quad.heightImu))

      self.ui.homeLatitudeText.setText(str(self.thread.wm.quad.homeLatitude))
      self.ui.homeLongitudeText.setText(str(self.thread.wm.quad.homeLongitude))
      self.ui.homeAltitudeText.setText(str(self.thread.wm.quad.homeAltitude))


      #import random
      #self.thread.wm.quad.latitude += random.uniform(-0.000003, 0.000009) # Lembrete: GPS em quadrotor esta desativado
      #self.thread.wm.quad.longitude += random.uniform(-0.000003, 0.000009)
      lat = self.thread.wm.quad.latitude
      lng = self.thread.wm.quad.longitude
      heading = self.thread.wm.quad.heading

      cmd = "updateMarkerPos({0}, {1}, '{2}', {3});".format(lat, lng, self.thread.wm.quad.name, heading)
      self.ui.webView.page().mainFrame().evaluateJavaScript(cmd)
      self.ui.webView.page().mainFrame().evaluateJavaScript("updateFlighPath({0}, {1});".format(lat, lng))

      lat = []
      lng = []
      for waypoint in self.thread.wm.waypointList:
          lat.append(waypoint['Y'])
          lng.append(waypoint['X'])
      cmd = "updateMarkerWaypoint({0}, {1});".format(lat, lng)
      self.ui.webView.page().mainFrame().evaluateJavaScript(cmd)
    except RuntimeWarning():
      pass


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = ManUi()
  myapp.show()
  sys.exit(app.exec_())
