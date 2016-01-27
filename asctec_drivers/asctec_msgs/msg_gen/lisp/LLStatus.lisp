; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude LLStatus.msg.html

(cl:defclass <LLStatus> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (battery_voltage_1
    :reader battery_voltage_1
    :initarg :battery_voltage_1
    :type cl:fixnum
    :initform 0)
   (battery_voltage_2
    :reader battery_voltage_2
    :initarg :battery_voltage_2
    :type cl:fixnum
    :initform 0)
   (status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (cpu_load
    :reader cpu_load
    :initarg :cpu_load
    :type cl:fixnum
    :initform 0)
   (compass_enabled
    :reader compass_enabled
    :initarg :compass_enabled
    :type cl:fixnum
    :initform 0)
   (chksum_error
    :reader chksum_error
    :initarg :chksum_error
    :type cl:fixnum
    :initform 0)
   (flying
    :reader flying
    :initarg :flying
    :type cl:fixnum
    :initform 0)
   (motors_on
    :reader motors_on
    :initarg :motors_on
    :type cl:fixnum
    :initform 0)
   (flightMode
    :reader flightMode
    :initarg :flightMode
    :type cl:fixnum
    :initform 0)
   (up_time
    :reader up_time
    :initarg :up_time
    :type cl:fixnum
    :initform 0))
)

(cl:defclass LLStatus (<LLStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LLStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LLStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<LLStatus> is deprecated: use asctec_msgs-msg:LLStatus instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'battery_voltage_1-val :lambda-list '(m))
(cl:defmethod battery_voltage_1-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:battery_voltage_1-val is deprecated.  Use asctec_msgs-msg:battery_voltage_1 instead.")
  (battery_voltage_1 m))

(cl:ensure-generic-function 'battery_voltage_2-val :lambda-list '(m))
(cl:defmethod battery_voltage_2-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:battery_voltage_2-val is deprecated.  Use asctec_msgs-msg:battery_voltage_2 instead.")
  (battery_voltage_2 m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:status-val is deprecated.  Use asctec_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'cpu_load-val :lambda-list '(m))
(cl:defmethod cpu_load-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:cpu_load-val is deprecated.  Use asctec_msgs-msg:cpu_load instead.")
  (cpu_load m))

(cl:ensure-generic-function 'compass_enabled-val :lambda-list '(m))
(cl:defmethod compass_enabled-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:compass_enabled-val is deprecated.  Use asctec_msgs-msg:compass_enabled instead.")
  (compass_enabled m))

(cl:ensure-generic-function 'chksum_error-val :lambda-list '(m))
(cl:defmethod chksum_error-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:chksum_error-val is deprecated.  Use asctec_msgs-msg:chksum_error instead.")
  (chksum_error m))

(cl:ensure-generic-function 'flying-val :lambda-list '(m))
(cl:defmethod flying-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:flying-val is deprecated.  Use asctec_msgs-msg:flying instead.")
  (flying m))

(cl:ensure-generic-function 'motors_on-val :lambda-list '(m))
(cl:defmethod motors_on-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:motors_on-val is deprecated.  Use asctec_msgs-msg:motors_on instead.")
  (motors_on m))

(cl:ensure-generic-function 'flightMode-val :lambda-list '(m))
(cl:defmethod flightMode-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:flightMode-val is deprecated.  Use asctec_msgs-msg:flightMode instead.")
  (flightMode m))

(cl:ensure-generic-function 'up_time-val :lambda-list '(m))
(cl:defmethod up_time-val ((m <LLStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:up_time-val is deprecated.  Use asctec_msgs-msg:up_time instead.")
  (up_time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LLStatus>) ostream)
  "Serializes a message object of type '<LLStatus>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'battery_voltage_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'battery_voltage_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'status)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'cpu_load)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'compass_enabled)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'chksum_error)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'flying)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'motors_on)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'flightMode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'up_time)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LLStatus>) istream)
  "Deserializes a message object of type '<LLStatus>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'battery_voltage_1) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'battery_voltage_2) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cpu_load) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'compass_enabled) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'chksum_error) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'flying) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motors_on) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'flightMode) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'up_time) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LLStatus>)))
  "Returns string type for a message object of type '<LLStatus>"
  "asctec_msgs/LLStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LLStatus)))
  "Returns string type for a message object of type 'LLStatus"
  "asctec_msgs/LLStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LLStatus>)))
  "Returns md5sum for a message object of type '<LLStatus>"
  "e0dae36eea5774367686a40e1843c5e2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LLStatus)))
  "Returns md5sum for a message object of type 'LLStatus"
  "e0dae36eea5774367686a40e1843c5e2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LLStatus>)))
  "Returns full string definition for message of type '<LLStatus>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# battery voltages in mV~%int16 battery_voltage_1~%int16 battery_voltage_2~%# dont care~%int16 status~%# Controller cycles per second (should be about 1000)~%int16 cpu_load~%# dont care~%int8 compass_enabled~%int8 chksum_error~%int8 flying~%int8 motors_on~%int16 flightMode~%# Time motors are turning~%int16 up_time~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LLStatus)))
  "Returns full string definition for message of type 'LLStatus"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# battery voltages in mV~%int16 battery_voltage_1~%int16 battery_voltage_2~%# dont care~%int16 status~%# Controller cycles per second (should be about 1000)~%int16 cpu_load~%# dont care~%int8 compass_enabled~%int8 chksum_error~%int8 flying~%int8 motors_on~%int16 flightMode~%# Time motors are turning~%int16 up_time~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LLStatus>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
     2
     2
     1
     1
     1
     1
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LLStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'LLStatus
    (cl:cons ':header (header msg))
    (cl:cons ':battery_voltage_1 (battery_voltage_1 msg))
    (cl:cons ':battery_voltage_2 (battery_voltage_2 msg))
    (cl:cons ':status (status msg))
    (cl:cons ':cpu_load (cpu_load msg))
    (cl:cons ':compass_enabled (compass_enabled msg))
    (cl:cons ':chksum_error (chksum_error msg))
    (cl:cons ':flying (flying msg))
    (cl:cons ':motors_on (motors_on msg))
    (cl:cons ':flightMode (flightMode msg))
    (cl:cons ':up_time (up_time msg))
))
