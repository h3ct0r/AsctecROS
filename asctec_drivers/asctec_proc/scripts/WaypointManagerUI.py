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
      self.wm.runUI()
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

    self.timer = QtCore.QTimer()
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.loop)

  def loadFinished(self):
      self.ui.quadNameText.setText(self.thread.wm.quad.name)
      self.ui.webView.page().mainFrame().evaluateJavaScript("initWaypointMarker({0});".format(self.thread.wm.waypointListSize))
      self.ui.heightSlider.setValue(self.thread.wm.quad.height)
      self.ui.heightSlider.valueChanged.connect(self.heightSliderEvent)
      self.ui.velocitySlider.setValue(self.thread.wm.quad.velocity)
      self.ui.velocitySlider.valueChanged.connect(self.velocitySliderEvent)

      self.ui.flightPathCheckbox.clicked.connect(self.flightPathCheckboxEvent)
      self.ui.quadrotorCheckbox.clicked.connect(self.quadrotorCheckboxEvent)
      self.ui.waypointCheckbox.clicked.connect(self.waypointCheckboxEvent)

      self.timer.start(200)

      self.ui.launchButton.clicked.connect(self.launchButtonEvent)
      self.ui.setHomeButton.clicked.connect(self.setHomeButtonEvent)
      self.ui.startWaypointListButton.clicked.connect(self.startWaypointListButtonEvent)
      self.ui.comeHomeButton.clicked.connect(self.comeHomeButtonEvent)
      self.ui.landButton.clicked.connect(self.landButtonEvent)
      self.ui.autonomousNavigationButton.clicked.connect(self.autonomousNavigationButtonEvent)

  def velocitySliderEvent(self):
      self.thread.wm.quad.velocity = self.ui.velocitySlider.value()

  def heightSliderEvent(self):
      self.thread.wm.quad.height = self.ui.heightSlider.value()

  def autonomousNavigationButtonEvent(self):
    self.ui.autonomousNavigationButton.setEnabled(False)
    self.ui.launchButton.setEnabled(False)
    self.ui.setHomeButton.setEnabled(False)
    self.ui.startWaypointListButton.setEnabled(False)
    self.ui.comeHomeButton.setEnabled(True)
    self.ui.landButton.setEnabled(True)
    self.thread.wm.managerStatus = 2
    # set state to 2


  def launchButtonEvent(self):
    self.ui.launchButton.setEnabled(False)
    self.ui.autonomousNavigationButton.setEnabled(False)
    self.ui.setHomeButton.setEnabled(True)
    self.ui.startWaypointListButton.setEnabled(False)
    self.ui.comeHomeButton.setEnabled(False)
    self.ui.landButton.setEnabled(True)
    self.thread.wm.managerStatus = 1
    # set state to 1

  def setHomeButtonEvent(self):
    self.ui.launchButton.setEnabled(False)
    self.ui.autonomousNavigationButton.setEnabled(False)
    self.ui.setHomeButton.setEnabled(False)
    self.ui.startWaypointListButton.setEnabled(True)
    self.ui.comeHomeButton.setEnabled(True)
    self.ui.landButton.setEnabled(True)
    self.thread.wm.managerStatus = 5
    # set state to 5

  def startWaypointListButtonEvent(self):
    self.ui.launchButton.setEnabled(False)
    self.ui.autonomousNavigationButton.setEnabled(False)
    self.ui.setHomeButton.setEnabled(False)
    self.ui.startWaypointListButton.setEnabled(False)
    self.ui.comeHomeButton.setEnabled(True)
    self.ui.landButton.setEnabled(True)
    self.thread.wm.managerStatus = 6
    # set state to 6

  def comeHomeButtonEvent(self):
    self.ui.launchButton.setEnabled(False)
    self.ui.autonomousNavigationButton.setEnabled(False)
    self.ui.setHomeButton.setEnabled(False)
    self.ui.startWaypointListButton.setEnabled(True)
    self.ui.comeHomeButton.setEnabled(False)
    self.ui.landButton.setEnabled(True)
    self.thread.wm.managerStatus = 3
    # set state to 3

  def landButtonEvent(self):
    self.ui.launchButton.setEnabled(True)
    self.ui.autonomousNavigationButton.setEnabled(True)
    self.ui.setHomeButton.setEnabled(False)
    self.ui.startWaypointListButton.setEnabled(False)
    self.ui.comeHomeButton.setEnabled(False)
    self.ui.landButton.setEnabled(False)
    self.thread.wm.managerStatus = 0
    # set state to 4


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

  def loop(self):
    try:
      if self.thread.wm.managerStatus is 0:
        self.ui.launchButton.setEnabled(True)
        self.ui.autonomousNavigationButton.setEnabled(True)

      self.ui.batteryBar.setValue(self.thread.wm.quad.batteryPercent)
      self.ui.navigationStatusText.setText(str(self.thread.wm.quad.navStatus))
      self.ui.batteryText.setText(str(self.thread.wm.quad.battery))

      currentWaypointIndex = self.thread.wm.currentWaypointIndex
      self.ui.waypointIndexText.setText(str(currentWaypointIndex+1) + " of " + str(self.thread.wm.waypointListSize))
      self.ui.waypointDistanceText.setText(str(self.thread.wm.quad.distanceToWp))
      self.ui.waypointLatitudeText.setText(str(self.thread.wm.waypointList[currentWaypointIndex]['lng']))
      self.ui.waypointLongitudeText.setText(str(self.thread.wm.waypointList[currentWaypointIndex]['lat']))
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

      self.ui.managerStatusText.setText(str(self.thread.wm.managerStatus))

      lat = self.thread.wm.quad.latitude
      lng = self.thread.wm.quad.longitude
      heading = self.thread.wm.quad.heading

      cmd = "updateMarkerPos({0}, {1}, '{2}', {3});".format(lat, lng, self.thread.wm.quad.name, heading)
      self.ui.webView.page().mainFrame().evaluateJavaScript(cmd)
      self.ui.webView.page().mainFrame().evaluateJavaScript("updateFlighPath({0}, {1});".format(lat, lng))
      self.thread.wm.quad.logFile.write(str(lat) + ', ' + str(lng) + ', ' + str(self.thread.wm.quad.heightImu) + '\n')

      lat = []
      lng = []
      for waypoint in self.thread.wm.waypointList:
          lat.append(waypoint['lat'])
          lng.append(waypoint['lng'])
      cmd = "updateMarkerWaypoint({0}, {1});".format(lat, lng)
      self.ui.webView.page().mainFrame().evaluateJavaScript(cmd)
    except RuntimeWarning():
      pass


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = ManUi()
  myapp.show()
  sys.exit(app.exec_())
