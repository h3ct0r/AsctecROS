Header header

#always set to 1
uint8 wp_number

#don't care
uint8 dummy_1
uint16 dummy_2

#see WPPROP defines below
uint8 properties

#max speed to travel to waypoint in % (default 100)
uint8 max_speed

#time to stay at a waypoint (XYZ) in 1/100th s
uint16 time

#position accuracy to consider a waypoint reached in mm (default: 2500 (= 2.5 m))
uint16 pos_acc

#chksum = 0xAAAA + wp.yaw + wp.height + wp.time + wp.X + wp.Y + wp.max_speed + wp.pos_acc + wp.properties + wp.wp_number
int16 chksum

#waypoint coordinates in mm; longitude in abs coords
int32 X

#waypoint coordinates in mm; latitude in abs coords
int32 Y

#Desired heading at waypoint
int32 yaw

#height over 0 reference in mm
int32 height

uint32 WPPROP_ABSCOORDS=1
uint32 WPPROP_HEIGHTENABLED=2
uint32 WPPROP_YAWENABLED=4
uint32 WPPROP_AUTOMATICGOTO=16
uint32 WPPROP_CAM_TRIGGER=32
