#!/usr/bin/python

import roslib; roslib.load_manifest('asctec_mon')
import rospy
import sys

from asctec_msgs.msg import LLStatus
from asctec_msgs.msg import IMUCalcData
from asctec_msgs.msg import GPSData
from asctec_msgs.msg import CurrentWay
from asctec_msgs.msg import WaypointData
from asctec_msgs.msg import WaypointCommand

import struct
import binascii
import os
import math
import time
import datetime

WAYPOINT_VEL = 1 # 0..100%

MIN_ALT_REF = -30.0
MAX_ALT_REF =  30.0
MIN_YAW_REF =  0.0
MAX_YAW_REF = 360.0

# if set waypoint is interpreted as absolute coordinates, else relative coords
WPPROP_ABSCOORDS         = 0x01
# set new height at waypoint
WPPROP_HEIGHTENABLED     = 0x02
# set new yaw-angle at waypoint (not yet implemented)
WPPROP_YAWENABLED         = 0x04
# if set, vehicle will not wait for a goto command, but goto this waypoint directly
WPPROP_AUTOMATICGOTO     = 0x10
# if set, photo camera is triggered when waypoint is reached and time to stay is 80% up (not available on pelican!)
WPPROP_CAM_TRIGGER         = 0x20

nav_status = 0
lat_val = 0
lon_val = 0
height_val = 0
heading_val = 0
battery_val = 0
distance_to_wp = 0

min_distance_inside_waypoint = 60

'''
Campo de futebol pequeno
# X is longitude
# Y is latitude
waypointList = [
    {'X': -43.960432, 'Y': -19.861114, 'Z': 2},
    {'X': -43.960288, 'Y': -19.860861, 'Z': 2},
    {'X': -43.960597, 'Y': -19.861023, 'Z': 2},
    {'X': -43.960338, 'Y': -19.861279, 'Z': 2},
    {'X': -43.960124, 'Y': -19.861234, 'Z': 2}
]
'''

#Campo de futebol grande
# X is longitude
# Y is latitude
#waypointList = [
#    {'X': -43.958376, 'Y': -19.869574, 'Z': 2},
#    {'X': -43.958081, 'Y': -19.869348, 'Z': 2},
#    {'X': -43.957749, 'Y': -19.869736, 'Z': 2},
#    {'X': -43.958048, 'Y': -19.869963, 'Z': 2},
#    {'X': -43.958046, 'Y': -19.869642, 'Z': 2}
#]

# Small square center of futball field
'''
waypointList = [
    {'X': -43.957929611206055, 'Y': -19.869701638874098, 'Z': 2},
    {'X': -43.95807445049285, 'Y': -19.869540196761694, 'Z': 2},
    {'X': -43.95796447992324, 'Y': -19.869739476845407, 'Z': 2},
    {'X': -43.95811200141907, 'Y': -19.86957551223782, 'Z': 2},
    {'X': -43.95800203084946, 'Y': -19.869777314807695, 'Z': 2},
    {'X': -43.958149552345276, 'Y': -19.869613350239256, 'Z': 2},
    {'X': -19.86981767529084, 'Y': -43.95803689956665, 'Z': 2},
    {'X': -43.958187103271484, 'Y': -19.86964866569908, 'Z': 2}
]
'''

'''
# Points in the reitoria
waypointList = [
    {'X': -43.96395117044449, 'Y': -19.866805746010677, 'Z': 2},
    {'X': -43.96409064531326, 'Y': -19.866588804171858, 'Z': 2},
    {'X': -43.96390289068222, 'Y': -19.866505558968868, 'Z': 2},
    {'X': -43.96387338638306, 'Y': -19.866548442866783, 'Z': 2},
    {'X': -43.96421402692795, 'Y': -19.866697275128367, 'Z': 2},
    {'X': -43.964179158210754, 'Y': -19.866737636395566, 'Z': 2},
    {'X': -43.96384388208389, 'Y': -19.866591326753095, 'Z': 2},
    {'X': -43.96381437778473, 'Y': -19.866634210627804, 'Z': 2},
    {'X': -43.964141607284546, 'Y': -19.866777997652502, 'Z': 2},
    {'X': -43.96399140357971, 'Y': -19.866767907339213, 'Z': 2},
    {'X': -43.96378755569458, 'Y': -19.86667709449091, 'Z': 2},
    {'X': -43.963758051395416, 'Y': -19.866719978342427, 'Z': 2},
    {'X': -43.96395117044449, 'Y': -19.866805746010677, 'Z': 2}
]
'''

'''
# Waypoints potential field campo futebol
waypointList = [
    {'X': -43.958192467689514, 'Y': -19.86944686296547, 'Z': 2},
{'X': -43.957945704460144, 'Y': -19.86944686296547, 'Z': 2},
{'X': -43.958192467689514, 'Y': -19.869686503683038, 'Z': 2},
{'X': -43.957945704460144, 'Y': -19.869686503683038, 'Z': 2},
{'X': -43.95813077688217, 'Y': -19.869726864189296, 'Z': 2},
{'X': -43.957934975624084, 'Y': -19.869724341657957, 'Z': 2},
{'X': -43.95813345909119, 'Y': -19.869911008868762, 'Z': 2},
{'X': -43.95794302225113, 'Y': -19.869885783582838, 'Z': 2},
{'X': -43.958192467689514, 'Y': -19.86944686296547, 'Z': 2}
]
'''
# Waypoints potential field campo futebol 2, com uma melhor disposicao que os anteriores
'''
waypointList = [
    {'Y': -43.958192467689514, 'X': -19.86944686296547, 'Z': 2},
    {'Y': -43.957945704460144, 'X': -19.86944686296547, 'Z': 2},
    {'Y': -43.957945704460144, 'X': -19.869686503683038, 'Z': 2},
    {'Y': -43.958192467689514, 'X': -19.869686503683038, 'Z': 2},
    {'Y': -43.957934975624084, 'X': -19.869724341657957, 'Z': 2},
    {'Y': -43.95813077688217, 'X': -19.869726864189296, 'Z': 2},
    {'Y': -43.95813345909119, 'X': -19.869911008868762, 'Z': 2},
    {'Y': -43.95794302225113, 'X': -19.869885783582838, 'Z': 2},
    {'Y': -43.958192467689514, 'X': -19.86944686296547, 'Z': 2}
]
'''

# Hexagono campo de futebol bandeixao
'''
waypointList = [
    {'X': -43.95809590816498, 'Y': -19.869439295357967, 'Z': 2},
    {'X': -43.957940340042114, 'Y': -19.869525061555223, 'Z': 2},
    {'X': -43.957892060279846, 'Y': -19.869610827706094, 'Z': 2},
    {'X': -43.958203196525574, 'Y': -19.869439295357967, 'Z': 2},
    {'X': -43.95823001861572, 'Y': -19.869484700997592, 'Z': 2},
    {'X': -43.95791351795196, 'Y': -19.8696562332966, 'Z': 2},
    {'X': -43.957940340042114, 'Y': -19.869701638874098, 'Z': 2},
    {'X': -43.9582622051239, 'Y': -19.869525061555223, 'Z': 2},
    {'X': -43.95828902721405, 'Y': -19.86956542210259, 'Z': 2},
    {'X': -43.95796716213226, 'Y': -19.869741999376505, 'Z': 2},
    {'X': -43.957993984222405, 'Y': -19.86978740492944, 'Z': 2},
    {'X': -43.9583158493042, 'Y': -19.869610827706094, 'Z': 2},
    {'X': -43.95826756954193, 'Y': -19.86969659381057, 'Z': 2},
    {'X': -43.95810127258301, 'Y': -19.86978740492944, 'Z': 2},
    {'X': -43.9582085609436, 'Y': -19.86978740492944, 'Z': 2}
]
'''

# Hexagono futebol embaixo

waypointList = [
{'X': -43.96034896373749, 'Y': -19.860928030822325, 'Z': 2},
{'X': -43.960193395614624, 'Y': -19.861013801622978, 'Z': 2},
{'X': -43.960145115852356, 'Y': -19.861099572377256, 'Z': 2},
{'X': -43.96045625209808, 'Y': -19.860928030822325, 'Z': 2},
{'X': -43.96048307418823, 'Y': -19.860973438899045, 'Z': 2},
{'X': -43.960166573524475, 'Y': -19.861144980404855, 'Z': 2},
{'X': -43.960193395614624, 'Y': -19.861190388419462, 'Z': 2},
{'X': -43.96051526069641, 'Y': -19.861013801622978, 'Z': 2},
{'X': -43.96054208278655, 'Y': -19.861054164336647, 'Z': 2},
{'X': -43.960220217704766, 'Y': -19.861230751088193, 'Z': 2},
{'X': -43.96024703979492, 'Y': -19.861276159078248, 'Z': 2},
{'X': -43.96056890487671, 'Y': -19.861099572377256, 'Z': 2},
{'X': -43.96052062511444, 'Y': -19.86118534308515, 'Z': 2},
{'X': -43.96035432815552, 'Y': -19.861276159078248, 'Z': 2},
{'X': -43.960461616516106, 'Y': -19.861276159078248, 'Z': 2}
]


class Waypoint:
    def __init__(self, x=0.0, y=0.0, z=0.0, heading=0.0):
       
        self.wp_number    = 1 # always 1
        self.dummy_1     = 0 # (don't care)
        self.dummy_2    = 0 # (don't care)
        self.properties    = WPPROP_ABSCOORDS + WPPROP_YAWENABLED + WPPROP_AUTOMATICGOTO
        #+ WPPROP_AUTOMATICGOTO
        #self.properties    = WPPROP_AUTOMATICGOTO
        #WPPROP_HEIGHTENABLED +
        self.max_speed     = WAYPOINT_VEL # 0-100%
        self.time         = 500 # in 1/100th s
        self.pos_acc     = 1500 # (2m) in mm, how close it can be to be 'at the waypoint'
       
        #Waypoint initialization
        self.X =         int(x*(10**7)) # [mm]
        self.Y =         int(y*(10**7)) # [mm]
       
        ############################
        # limita referencia de altitude
        if z < MIN_ALT_REF:
            z = MIN_ALT_REF
        if z > MAX_ALT_REF:
            z = MAX_ALT_REF
           
        self.height =    int(z*1000) # [mm]
        ############################
        # limita yaw
        if heading < MIN_YAW_REF:
            heading = MIN_YAW_REF
        if heading > MAX_YAW_REF:
            heading = MAX_YAW_REF
       
        self.yaw =     int(heading*1000) # [deg*1000]
        ############################
        self.chksum = 0
        ############################
        self.zref = 0
        self.chksum_short = 0
       
    #########################################################################
    # cria waypoint para mandar
    # number: 1..n
    # x, y, z: [m]
    # heading: [deg]
    #########################################################################
    def get_Waypoint(self, zCurrent, zInit):
       
        zCurrent = int(zCurrent*1000)     # altitude corrente do quadrotor
        zInit = int(zInit*1000)            # altitude inicial dada
       
        # calcula um novo zref baseado na altitude do quadrotor
        zref =  self.height + zInit # referencia relativa a condicao inicial
        zref = zref + .2*(zref - zCurrent) # fator de correcao proporcional
       
        # limita referencia de altitude
        if zref < (1000*MIN_ALT_REF):
            zref = (1000*MIN_ALT_REF)
        if zref > (1000*MAX_ALT_REF):
            zref = (1000*MAX_ALT_REF)
           
        #print self.height/1000.0, zref/1000.0
       
        # calcula o checksum
        self.chksum = (0xaaaa+self.yaw+ zref +self.time+self.X+self.Y+self.max_speed+self.pos_acc+self.properties+self.wp_number)
        # delimita o checksum
        self.chksum = self.chksum % 32768
       
        #B = unsigned char, H = unsigned short, h = short, 4i = four int's g iiii)
        New_position = struct.Struct('BBHBBHHh4i')

        # '{yaw: 0, height: 5000, time: 500, X: 10000, Y: 0, max_speed: 100, pos_acc: 2500, properties: 16, wp_number: 1, dummy_1: 0, dummy_2: 0, chksum: 61807}'
        self.zref = zref

        checksum = struct.Struct('h')
        checksum = checksum.pack(self.chksum)
        #print "unpack! ",struct.unpack('H', checksum);


        hexstring = binascii.hexlify(checksum)
        hexlist = [hexstring[i:i+2] for i in range(0,len(hexstring), 2)]
        hexlistreversed = list(reversed(hexlist))
        inthexreversed = ''.join(hexlistreversed)
        x = int(hexstring, 16)
        #print "chcksum :",hexstring, "int :", x, " hexlistreversed :", inthexreversed, 16
        self.chksum_short = struct.unpack('h', checksum)[0]
        #self.chksum_short = x

        return New_position.pack(    self.wp_number,        # B = unsigned char
                                    self.dummy_1,        # B = unsigned char
                                    self.dummy_2,        # H = unsigned short
                                    self.properties,    # B = unsigned char
                                    self.max_speed,        # B = unsigned char
                                    self.time,            # H = unsigned short
                                    self.pos_acc,        # H = unsigned short
                                    self.chksum,        # H = unsigned short (e nao h = short)
                                    self.X,             # i = int
                                    self.Y,             # i = int
                                    self.yaw,            # i = int
                                    zref) #self.height)        # i = int
                                       
    #########################################################################
    def show(self):   
        print "x = " + str(self.X) + "\ty = " + str(self.Y) + "\tz = " + str(self.height) + "\tyaw = " + str(self.yaw)

    def generateWPforROSPublish(self):   
        rosCommand = "'{wp_number: "+str(self.wp_number)+", dummy_1: 0, dummy_2: 0, properties: "+str(self.properties)+", max_speed: "+str(self.max_speed)+", time: "+str(self.time)+", pos_acc: "+str(self.pos_acc)+", chksum: "+str(self.chksum_short)+", X: "+str(self.X)+", Y: "+str(self.Y)+", yaw: "+str(self.yaw)+", height: "+str(int(self.zref))+"'}"
        return rosCommand

    def getValuesAsDict(self):
        return {'wp_number': self.wp_number, 'dummy_1': 0, 'dummy_2': 0, 'properties': self.properties, 'max_speed': self.max_speed, 'time': self.time, 'pos_acc': self.pos_acc, 'chksum': self.chksum_short, 'X': self.X, 'Y': self.Y, 'yaw': self.yaw, 'height': self.zref }

    def getWaypointStruct(self):
        wp_data = WaypointData()

        wp_data.wp_number = self.wp_number
        wp_data.dummy_1 = self.dummy_1
        wp_data.dummy_2 = self.dummy_2
        wp_data.properties = self.properties
        wp_data.max_speed = self.max_speed
        wp_data.time = self.time
        wp_data.pos_acc = self.pos_acc
        wp_data.chksum = self.chksum_short
        wp_data.X = self.X
        wp_data.Y = self.Y
        wp_data.yaw = self.yaw
        wp_data.height = self.zref

        return wp_data
    #########################################################################

def gps_callback(data):
    global lat_val, lon_val, height_val, heading_val

    lat_val = float(data.latitude)/float(10**7)
    lon_val = float(data.longitude)/float(10**7)
    height_val = float(data.height)/1000.0
    heading_val = float(data.heading)/1000.0

    #print 'Lat: {0:+12.7f}'.format(lat_val)
    #print 'Lon: {0:+12.7f}'.format(lon_val)
    #print 'Height: {0: 7.3f}m'.format(height_val)
    #print 'Heading: {0: 7.3f}'.format(heading_val)

def ll_callback(data):
    global battery_val
    battery_val = float(data.battery_voltage_1)/1000.0
    #print 'Battery: {0:.3f}V'.format(battery_val)

def currentw_callback(data):
    global nav_status, distance_to_wp
    nav_status = int(data.navigation_status)
    distance_to_wp = float(data.distance_to_wp)*float(10)

    #print 'Nav status: '+str(nav_status)
    #print 'Distance to WP in CM: {0:.1f}'.format(distance_to_wp)

def publish_next_waypoint(waypoint_cmd_publisher, waypoint_data_publisher):
    print "PUBLISHING WAYPOINT"

    wp_command = WaypointCommand()
    wp_command.cmd = ">*>wg"
    wp_command.header.stamp = rospy.get_rostime()
    waypoint_cmd_publisher.publish(wp_command)

    current_wp = waypointList.pop(0)
    wp = Waypoint(current_wp['X'], current_wp['Y'], current_wp['Z'], 0)
    wp.get_Waypoint(0, 500)
    #print wp.generateWPforROSPublish()
    waypoint_data = wp.getWaypointStruct()
    waypoint_data.header.stamp = rospy.get_rostime()
    waypoint_data_publisher.publish(waypoint_data)

    #print "WAYPOINT PUBLISHED",wp_command, waypoint_data
    print "WAYPOINT PUBLISHED"

def publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index):
    print "PUBLISHING WAYPOINT"

    wp_command = WaypointCommand()
    wp_command.cmd = ">*>wg"
    wp_command.header.stamp = rospy.get_rostime()
    waypoint_cmd_publisher.publish(wp_command)

    current_wp = waypointList[waypoint_index]
    wp = Waypoint(current_wp['X'], current_wp['Y'], current_wp['Z'], 0)
    wp.get_Waypoint(0, 500)
    #print wp.generateWPforROSPublish()
    waypoint_data = wp.getWaypointStruct()
    waypoint_data.header.stamp = rospy.get_rostime()
    waypoint_data_publisher.publish(waypoint_data)

    #print "WAYPOINT PUBLISHED",wp_command, waypoint_data
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
    return d * 100


def initialize_node():
    global nav_status, distance_to_wp, battery_val, lat_val, lon_val, height_val, heading_val
    rospy.init_node('waypoint_manager')
   
    rospy.Subscriber("asctec/LL_STATUS", LLStatus, ll_callback)
    rospy.Subscriber("asctec/GPS_DATA", GPSData, gps_callback)
    rospy.Subscriber("asctec/CURRENT_WAY", CurrentWay, currentw_callback)
   
    waypoint_cmd_publisher = rospy.Publisher('/asctec/WAYCOMMAND', WaypointCommand)
    waypoint_data_publisher = rospy.Publisher('/asctec/WAYPOINT', WaypointData)

    rospy.sleep(3)
    r = rospy.Rate(2)

    waypoint_index = 0
    publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)

    r.sleep()

    while not rospy.is_shutdown():
        os.system('clear') # Clear the shell

        current_wp = waypointList[waypoint_index]
        distance_calculated = dist(lat_val, lon_val, current_wp['Y'], current_wp['X'])

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        print st
        print "Distance calculated in CM:", distance_calculated
        print "Distance generated by UAV:", distance_to_wp
        print "Navigation status        :", nav_status
        print "Battery values           :", battery_val
        print "Current waypoint Number  :", waypoint_index
        print "Current waypoint         :", current_wp['Y'], current_wp['X']

        #if(distance_to_wp <= min_distance_inside_waypoint):
        if nav_status == 7:
            print "        ** Distance inside waypoint reached!"
           
            if(waypoint_index >= len(waypointList)):
                print "        ** No more waypoints to send!"
                print "        ** Program terminated!"
                return 0
            else:
                waypoint_index += 1
                print "        ** Publishing waypoint [",waypoint_index,"]"
                publish_waypoint_by_index(waypoint_cmd_publisher, waypoint_data_publisher, waypoint_index)
                rospy.sleep(3)
        r.sleep()

if __name__ == "__main__":
    initialize_node()
    rospy.spin()