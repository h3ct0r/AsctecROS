#!/usr/bin/python
import struct
import binascii
from asctec_msgs.msg import WaypointData

# if set waypoint is interpreted as absolute coordinates, else relative coords
WPPROP_ABSCOORDS 		= 0x01
# set new height at waypoint
WPPROP_HEIGHTENABLED 	= 0x02
# set new yaw-angle at waypoint (not yet implemented)
WPPROP_YAWENABLED 		= 0x04
# if set, vehicle will not wait for a goto command, but goto this waypoint directly
WPPROP_AUTOMATICGOTO 	= 0x10
# if set, photo camera is triggered when waypoint is reached and time to stay is 80% up (not available on pelican!)
WPPROP_CAM_TRIGGER 		= 0x20

MIN_YAW_REF =  0.0
MAX_YAW_REF = 360.0

class Waypoint:
	def __init__(self, x=0.0, y=0.0, z=0.0, heading=0.0, velocity=0, waypointTime=1):
		
		self.wp_number	= 1 # always 1
		self.dummy_1 	= 0 # (don't care)
		self.dummy_2	= 0 # (don't care)
		self.properties	= WPPROP_ABSCOORDS + WPPROP_YAWENABLED + WPPROP_HEIGHTENABLED
		# + WPPROP_YAWENABLED
		#+ WPPROP_AUTOMATICGOTO
		#self.properties	= WPPROP_AUTOMATICGOTO 
		#WPPROP_HEIGHTENABLED + 
		# Velocidade do quadrotor de 0 a 3m/s
		self.max_speed 	= velocity # 0-100%
		#Tempo que o Quadrotor fica no waypoint
		self.time 		= waypointTime * 100 # in 1/100th s
		self.pos_acc 	= 2000 # (2m) in mm, how close it can be to be 'at the waypoint'
		
		#Waypoint initialization
		# X is Longitude, Y is Latitude
		self.X = 		int(x*(10**7)) # [mm]
		self.Y = 		int(y*(10**7)) # [mm]
		
		# self.height =	int(z*1000) # [mm]
		self.height = int(z) # [mm]
		############################
		if heading < MIN_YAW_REF:
			heading = MIN_YAW_REF
		if heading > MAX_YAW_REF:
			heading = MAX_YAW_REF

		self.yaw = 	int(heading*1000) # [deg*1000]
		############################
		self.chksum = 0
		############################
		self.chksum_short = 0

		
	#########################################################################
	# cria waypoint para mandar
	# number: 1..n
	# x, y, z: [m]
	# heading: [deg]
	#########################################################################
	def getWaypoint(self):

		# calcula o checksum with absolute coordinates (lat and long)
		self.chksum = (0xaaaa+ self.yaw + self.height +self.time+self.X+self.Y+self.max_speed+self.pos_acc+self.properties+self.wp_number)
		#  Calculates cksum with
		# self.chksum = (0xAAAA+ self.yaw + 5000 +self.time+(self.X/(10**7))+(self.Y/(10**7))+self.max_speed+self.pos_acc+self.properties+self.wp_number)
		# delimita o checksum

		self.chksum = self.chksum % 32768

		#B = unsigned char, H = unsigned short, h = short, 4i = four int's g iiii)
		New_position = struct.Struct('BBHBBHHh4i')

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


		return New_position.pack(	self.wp_number,		# B = unsigned char
									self.dummy_1,		# B = unsigned char
									self.dummy_2,		# H = unsigned short
									self.properties,	# B = unsigned char
									self.max_speed,		# B = unsigned char
									self.time,			# H = unsigned short
									self.pos_acc,		# H = unsigned short
									self.chksum,		# H = unsigned short (e nao h = short)
									self.X, 			# i = int
									self.Y, 			# i = int
									self.yaw,			# i = int 
									self.height)		# i = int

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
		wp_data.height = self.height
		# self.show()		

		return wp_data
										
	#########################################################################
	# def show(self):	
	# 	# print "x = " + str(self.X) + "\ty = " + str(self.Y) + "\tz = " + str(self.height) + "\tyaw = " + str(self.yaw)
	# 	print "\nDENTRO DO publish_waypoint_by_index()"
	# 	print "wp_number: ", self.wp_number
	# 	print "dummy 1: ", self.dummy_1
	# 	print "dummy 2: ", self.dummy_2
	# 	print "properties: ", self.properties
	# 	print "max_speed: ", self.max_speed
	# 	print "time at waypoint: ", self.time
	# 	print "position accuracy: ", self.pos_acc
	# 	print "chksum: ", self.chksum_short
	# 	print "X: ", self.X
	# 	print "Y: ", self.Y
	# 	print "yaw: ", self.yaw
	# 	print "height: ", self.height

	#def generateWPforROSPublish(self):	
	#	rosCommand = "'{wp_number: "+str(self.wp_number)+", dummy_1: 0, dummy_2: 0, properties: "+str(self.properties)+", max_speed: "+str(self.max_speed)+", time: "+str(self.time)+", pos_acc: "+str(self.pos_acc)+", chksum: "+str(self.chksum_short)+", X: "+str(self.X)+", Y: "+str(self.Y)+", yaw: "+str(self.yaw)+", height: "+str(int(self.zref))+"'}"
	#	return rosCommand

	#def getValuesAsDict(self):
	#	return {'wp_number': self.wp_number, 'dummy_1': 0, 'dummy_2': 0, 'properties': self.properties, 'max_speed': self.max_speed, 'time': self.time, 'pos_acc': self.pos_acc, 'chksum': self.chksum_short, 'X': self.X, 'Y': self.Y, 'yaw': self.yaw, 'height': self.height}


