#!/usr/bin/python

import sys
import numpy as np
from PyQt4 import QtCore, QtGui
from interface import Ui_MainWindow
from gmaps import html

class WaypointGenerator(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pointsList = np.matrix([])
        # here we connect signals with our slots
        self.ui.webView.setHtml(html)
        self.ui.webView.loadFinished.connect(self.loadFinished)

        QtCore.QObject.connect(self.ui.loadButton, QtCore.SIGNAL("clicked()"), self.getPoints)
        QtCore.QObject.connect(self.ui.plotButton, QtCore.SIGNAL("clicked()"), self.plotWaypoints)
        QtCore.QObject.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"), self.saveWaypoints)

        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.loop)

    def loadFinished(self):
        self.isPloted = False
        self.theta = 0
        self.timer.start(20)

    def loop(self):
        if len(self.pointsList) > 1 and not self.isPloted:
            self.theta = self.ui.verticalSlider.value() - self.theta
            z = (np.pi * self.theta)/float(180)
            rot = np.matrix([[np.cos(z), -np.sin(z)], [np.sin(z), np.cos(z)]])
            size = len(self.pointsList[:,0].tolist())
            mx = (sum(self.pointsList[:,0])/size).tolist()
            my = (sum(self.pointsList[:,1])/size).tolist()
            m = [[mx[0][0], my[0][0]]]*size
            m = np.matrix(m)
            self.pointsList[:,0:2] = (self.pointsList[:,0:2] - m) * rot + m
            self.ui.webView.page().mainFrame().evaluateJavaScript("updateMarkerWaypoint({0}, {1});".format(self.pointsList[:, 0].tolist(), self.pointsList[:, 1].tolist()))
            self.theta = self.ui.verticalSlider.value()

    def plotWaypoints(self):
        self.isPloted = not self.isPloted
        if self.isPloted:
            s = self.ui.webView.page().mainFrame().evaluateJavaScript('getWaypointPloted();')
            self.waypointList = s.toPyObject()

    def getPoints(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            points = open(self.filename, 'r').read()
            points = points.split('\n')
            self.pointsList = []
            for p in points:
                p = p.split(',')
                for i  in range(len(p)):
                    p[i] = float(p[i])

                self.pointsList.append(p)

            self.pointsList = np.matrix(self.pointsList)
            self.isPloted = False
            self.ui.webView.page().mainFrame().evaluateJavaScript("initWaypointMarker({0});".format(len(self.pointsList)))

    def saveWaypoints(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getSaveFileName()
        s = open(self.filename, 'w')
        self.name = "/hum1"
        for i in range(len(self.waypointList)):
            l = self.name + ', ' + str(self.waypointList[i][0]) + ', ' + str(self.waypointList[i][1]) + ', ' + str(self.pointsList[i,2]*40000/255) + '\n'
            s.write(l)
        s.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = WaypointGenerator()
    myapp.show()
    sys.exit(app.exec_())
