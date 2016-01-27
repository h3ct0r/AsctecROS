; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude WaypointData.msg.html

(cl:defclass <WaypointData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (wp_number
    :reader wp_number
    :initarg :wp_number
    :type cl:fixnum
    :initform 0)
   (dummy_1
    :reader dummy_1
    :initarg :dummy_1
    :type cl:fixnum
    :initform 0)
   (dummy_2
    :reader dummy_2
    :initarg :dummy_2
    :type cl:fixnum
    :initform 0)
   (properties
    :reader properties
    :initarg :properties
    :type cl:fixnum
    :initform 0)
   (max_speed
    :reader max_speed
    :initarg :max_speed
    :type cl:fixnum
    :initform 0)
   (time
    :reader time
    :initarg :time
    :type cl:fixnum
    :initform 0)
   (pos_acc
    :reader pos_acc
    :initarg :pos_acc
    :type cl:fixnum
    :initform 0)
   (chksum
    :reader chksum
    :initarg :chksum
    :type cl:fixnum
    :initform 0)
   (X
    :reader X
    :initarg :X
    :type cl:integer
    :initform 0)
   (Y
    :reader Y
    :initarg :Y
    :type cl:integer
    :initform 0)
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0))
)

(cl:defclass WaypointData (<WaypointData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WaypointData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WaypointData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<WaypointData> is deprecated: use asctec_msgs-msg:WaypointData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'wp_number-val :lambda-list '(m))
(cl:defmethod wp_number-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:wp_number-val is deprecated.  Use asctec_msgs-msg:wp_number instead.")
  (wp_number m))

(cl:ensure-generic-function 'dummy_1-val :lambda-list '(m))
(cl:defmethod dummy_1-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:dummy_1-val is deprecated.  Use asctec_msgs-msg:dummy_1 instead.")
  (dummy_1 m))

(cl:ensure-generic-function 'dummy_2-val :lambda-list '(m))
(cl:defmethod dummy_2-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:dummy_2-val is deprecated.  Use asctec_msgs-msg:dummy_2 instead.")
  (dummy_2 m))

(cl:ensure-generic-function 'properties-val :lambda-list '(m))
(cl:defmethod properties-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:properties-val is deprecated.  Use asctec_msgs-msg:properties instead.")
  (properties m))

(cl:ensure-generic-function 'max_speed-val :lambda-list '(m))
(cl:defmethod max_speed-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:max_speed-val is deprecated.  Use asctec_msgs-msg:max_speed instead.")
  (max_speed m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:time-val is deprecated.  Use asctec_msgs-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'pos_acc-val :lambda-list '(m))
(cl:defmethod pos_acc-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:pos_acc-val is deprecated.  Use asctec_msgs-msg:pos_acc instead.")
  (pos_acc m))

(cl:ensure-generic-function 'chksum-val :lambda-list '(m))
(cl:defmethod chksum-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:chksum-val is deprecated.  Use asctec_msgs-msg:chksum instead.")
  (chksum m))

(cl:ensure-generic-function 'X-val :lambda-list '(m))
(cl:defmethod X-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:X-val is deprecated.  Use asctec_msgs-msg:X instead.")
  (X m))

(cl:ensure-generic-function 'Y-val :lambda-list '(m))
(cl:defmethod Y-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:Y-val is deprecated.  Use asctec_msgs-msg:Y instead.")
  (Y m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:yaw-val is deprecated.  Use asctec_msgs-msg:yaw instead.")
  (yaw m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <WaypointData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:height-val is deprecated.  Use asctec_msgs-msg:height instead.")
  (height m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<WaypointData>)))
    "Constants for message type '<WaypointData>"
  '((:WPPROP_ABSCOORDS . 1)
    (:WPPROP_HEIGHTENABLED . 2)
    (:WPPROP_YAWENABLED . 4)
    (:WPPROP_AUTOMATICGOTO . 16)
    (:WPPROP_CAM_TRIGGER . 32))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'WaypointData)))
    "Constants for message type 'WaypointData"
  '((:WPPROP_ABSCOORDS . 1)
    (:WPPROP_HEIGHTENABLED . 2)
    (:WPPROP_YAWENABLED . 4)
    (:WPPROP_AUTOMATICGOTO . 16)
    (:WPPROP_CAM_TRIGGER . 32))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WaypointData>) ostream)
  "Serializes a message object of type '<WaypointData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'wp_number)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy_1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy_2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'dummy_2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'properties)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'max_speed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pos_acc)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'pos_acc)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'chksum)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'X)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'Y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'yaw)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WaypointData>) istream)
  "Deserializes a message object of type '<WaypointData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'wp_number)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy_1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy_2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'dummy_2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'properties)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'max_speed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pos_acc)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'pos_acc)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'chksum) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'X) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yaw) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WaypointData>)))
  "Returns string type for a message object of type '<WaypointData>"
  "asctec_msgs/WaypointData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WaypointData)))
  "Returns string type for a message object of type 'WaypointData"
  "asctec_msgs/WaypointData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WaypointData>)))
  "Returns md5sum for a message object of type '<WaypointData>"
  "1aea889573a3c976bdc966a2229943a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WaypointData)))
  "Returns md5sum for a message object of type 'WaypointData"
  "1aea889573a3c976bdc966a2229943a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WaypointData>)))
  "Returns full string definition for message of type '<WaypointData>"
  (cl:format cl:nil "Header header~%~%#always set to 1~%uint8 wp_number~%~%#don't care~%uint8 dummy_1~%uint16 dummy_2~%~%#see WPPROP defines below~%uint8 properties~%~%#max speed to travel to waypoint in % (default 100)~%uint8 max_speed~%~%#time to stay at a waypoint (XYZ) in 1/100th s~%uint16 time~%~%#position accuracy to consider a waypoint reached in mm (default: 2500 (= 2.5 m))~%uint16 pos_acc~%~%#chksum = 0xAAAA + wp.yaw + wp.height + wp.time + wp.X + wp.Y + wp.max_speed + wp.pos_acc + wp.properties + wp.wp_number~%int16 chksum~%~%#waypoint coordinates in mm; longitude in abs coords~%int32 X~%~%#waypoint coordinates in mm; latitude in abs coords~%int32 Y~%~%#Desired heading at waypoint~%int32 yaw~%~%#height over 0 reference in mm~%int32 height~%~%uint32 WPPROP_ABSCOORDS=1~%uint32 WPPROP_HEIGHTENABLED=2~%uint32 WPPROP_YAWENABLED=4~%uint32 WPPROP_AUTOMATICGOTO=16~%uint32 WPPROP_CAM_TRIGGER=32~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WaypointData)))
  "Returns full string definition for message of type 'WaypointData"
  (cl:format cl:nil "Header header~%~%#always set to 1~%uint8 wp_number~%~%#don't care~%uint8 dummy_1~%uint16 dummy_2~%~%#see WPPROP defines below~%uint8 properties~%~%#max speed to travel to waypoint in % (default 100)~%uint8 max_speed~%~%#time to stay at a waypoint (XYZ) in 1/100th s~%uint16 time~%~%#position accuracy to consider a waypoint reached in mm (default: 2500 (= 2.5 m))~%uint16 pos_acc~%~%#chksum = 0xAAAA + wp.yaw + wp.height + wp.time + wp.X + wp.Y + wp.max_speed + wp.pos_acc + wp.properties + wp.wp_number~%int16 chksum~%~%#waypoint coordinates in mm; longitude in abs coords~%int32 X~%~%#waypoint coordinates in mm; latitude in abs coords~%int32 Y~%~%#Desired heading at waypoint~%int32 yaw~%~%#height over 0 reference in mm~%int32 height~%~%uint32 WPPROP_ABSCOORDS=1~%uint32 WPPROP_HEIGHTENABLED=2~%uint32 WPPROP_YAWENABLED=4~%uint32 WPPROP_AUTOMATICGOTO=16~%uint32 WPPROP_CAM_TRIGGER=32~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WaypointData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     2
     1
     1
     2
     2
     2
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WaypointData>))
  "Converts a ROS message object to a list"
  (cl:list 'WaypointData
    (cl:cons ':header (header msg))
    (cl:cons ':wp_number (wp_number msg))
    (cl:cons ':dummy_1 (dummy_1 msg))
    (cl:cons ':dummy_2 (dummy_2 msg))
    (cl:cons ':properties (properties msg))
    (cl:cons ':max_speed (max_speed msg))
    (cl:cons ':time (time msg))
    (cl:cons ':pos_acc (pos_acc msg))
    (cl:cons ':chksum (chksum msg))
    (cl:cons ':X (X msg))
    (cl:cons ':Y (Y msg))
    (cl:cons ':yaw (yaw msg))
    (cl:cons ':height (height msg))
))
