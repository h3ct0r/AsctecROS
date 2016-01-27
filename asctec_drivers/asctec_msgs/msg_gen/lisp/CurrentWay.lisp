; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude CurrentWay.msg.html

(cl:defclass <CurrentWay> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (dummy1
    :reader dummy1
    :initarg :dummy1
    :type cl:fixnum
    :initform 0)
   (properties
    :reader properties
    :initarg :properties
    :type cl:fixnum
    :initform 0)
   (nr_of_wp
    :reader nr_of_wp
    :initarg :nr_of_wp
    :type cl:fixnum
    :initform 0)
   (current_wp
    :reader current_wp
    :initarg :current_wp
    :type cl:fixnum
    :initform 0)
   (current_wp_memlocation
    :reader current_wp_memlocation
    :initarg :current_wp_memlocation
    :type cl:fixnum
    :initform 0)
   (status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (dummy2
    :reader dummy2
    :initarg :dummy2
    :type cl:fixnum
    :initform 0)
   (navigation_status
    :reader navigation_status
    :initarg :navigation_status
    :type cl:fixnum
    :initform 0)
   (distance_to_wp
    :reader distance_to_wp
    :initarg :distance_to_wp
    :type cl:fixnum
    :initform 0))
)

(cl:defclass CurrentWay (<CurrentWay>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CurrentWay>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CurrentWay)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<CurrentWay> is deprecated: use asctec_msgs-msg:CurrentWay instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'dummy1-val :lambda-list '(m))
(cl:defmethod dummy1-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:dummy1-val is deprecated.  Use asctec_msgs-msg:dummy1 instead.")
  (dummy1 m))

(cl:ensure-generic-function 'properties-val :lambda-list '(m))
(cl:defmethod properties-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:properties-val is deprecated.  Use asctec_msgs-msg:properties instead.")
  (properties m))

(cl:ensure-generic-function 'nr_of_wp-val :lambda-list '(m))
(cl:defmethod nr_of_wp-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:nr_of_wp-val is deprecated.  Use asctec_msgs-msg:nr_of_wp instead.")
  (nr_of_wp m))

(cl:ensure-generic-function 'current_wp-val :lambda-list '(m))
(cl:defmethod current_wp-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:current_wp-val is deprecated.  Use asctec_msgs-msg:current_wp instead.")
  (current_wp m))

(cl:ensure-generic-function 'current_wp_memlocation-val :lambda-list '(m))
(cl:defmethod current_wp_memlocation-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:current_wp_memlocation-val is deprecated.  Use asctec_msgs-msg:current_wp_memlocation instead.")
  (current_wp_memlocation m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:status-val is deprecated.  Use asctec_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'dummy2-val :lambda-list '(m))
(cl:defmethod dummy2-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:dummy2-val is deprecated.  Use asctec_msgs-msg:dummy2 instead.")
  (dummy2 m))

(cl:ensure-generic-function 'navigation_status-val :lambda-list '(m))
(cl:defmethod navigation_status-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:navigation_status-val is deprecated.  Use asctec_msgs-msg:navigation_status instead.")
  (navigation_status m))

(cl:ensure-generic-function 'distance_to_wp-val :lambda-list '(m))
(cl:defmethod distance_to_wp-val ((m <CurrentWay>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:distance_to_wp-val is deprecated.  Use asctec_msgs-msg:distance_to_wp instead.")
  (distance_to_wp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CurrentWay>) ostream)
  "Serializes a message object of type '<CurrentWay>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'properties)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'nr_of_wp)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'nr_of_wp)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_wp)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_wp_memlocation)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'navigation_status)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'navigation_status)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'distance_to_wp)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'distance_to_wp)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CurrentWay>) istream)
  "Deserializes a message object of type '<CurrentWay>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'properties)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'nr_of_wp)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'nr_of_wp)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_wp)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_wp_memlocation)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dummy2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'navigation_status)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'navigation_status)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'distance_to_wp)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'distance_to_wp)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CurrentWay>)))
  "Returns string type for a message object of type '<CurrentWay>"
  "asctec_msgs/CurrentWay")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CurrentWay)))
  "Returns string type for a message object of type 'CurrentWay"
  "asctec_msgs/CurrentWay")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CurrentWay>)))
  "Returns md5sum for a message object of type '<CurrentWay>"
  "6d25aae02ea1a55cb5a3abd0dd055622")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CurrentWay)))
  "Returns md5sum for a message object of type 'CurrentWay"
  "6d25aae02ea1a55cb5a3abd0dd055622")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CurrentWay>)))
  "Returns full string definition for message of type '<CurrentWay>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2014~%#  Hector Azpurua <hector.azpurua@dcc.ufmg.br>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# See http://asctec-users.986163.n3.nabble.com/How-to-see-if-the-UAV-has-reached-a-waypoint-td3245304.html~%# for clarification~%# _CurrentWay~%uint8 dummy1~%uint8 properties~%uint16 nr_of_wp~%uint8 current_wp~%uint8 current_wp_memlocation~%uint8 status~%uint8 dummy2~%uint16 navigation_status~%uint16 distance_to_wp~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CurrentWay)))
  "Returns full string definition for message of type 'CurrentWay"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2014~%#  Hector Azpurua <hector.azpurua@dcc.ufmg.br>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# See http://asctec-users.986163.n3.nabble.com/How-to-see-if-the-UAV-has-reached-a-waypoint-td3245304.html~%# for clarification~%# _CurrentWay~%uint8 dummy1~%uint8 properties~%uint16 nr_of_wp~%uint8 current_wp~%uint8 current_wp_memlocation~%uint8 status~%uint8 dummy2~%uint16 navigation_status~%uint16 distance_to_wp~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CurrentWay>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     2
     1
     1
     1
     1
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CurrentWay>))
  "Converts a ROS message object to a list"
  (cl:list 'CurrentWay
    (cl:cons ':header (header msg))
    (cl:cons ':dummy1 (dummy1 msg))
    (cl:cons ':properties (properties msg))
    (cl:cons ':nr_of_wp (nr_of_wp msg))
    (cl:cons ':current_wp (current_wp msg))
    (cl:cons ':current_wp_memlocation (current_wp_memlocation msg))
    (cl:cons ':status (status msg))
    (cl:cons ':dummy2 (dummy2 msg))
    (cl:cons ':navigation_status (navigation_status msg))
    (cl:cons ':distance_to_wp (distance_to_wp msg))
))
