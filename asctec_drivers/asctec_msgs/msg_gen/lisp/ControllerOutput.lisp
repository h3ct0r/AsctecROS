; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude ControllerOutput.msg.html

(cl:defclass <ControllerOutput> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (nick
    :reader nick
    :initarg :nick
    :type cl:integer
    :initform 0)
   (roll
    :reader roll
    :initarg :roll
    :type cl:integer
    :initform 0)
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:integer
    :initform 0)
   (thrust
    :reader thrust
    :initarg :thrust
    :type cl:integer
    :initform 0))
)

(cl:defclass ControllerOutput (<ControllerOutput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControllerOutput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControllerOutput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<ControllerOutput> is deprecated: use asctec_msgs-msg:ControllerOutput instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ControllerOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'nick-val :lambda-list '(m))
(cl:defmethod nick-val ((m <ControllerOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:nick-val is deprecated.  Use asctec_msgs-msg:nick instead.")
  (nick m))

(cl:ensure-generic-function 'roll-val :lambda-list '(m))
(cl:defmethod roll-val ((m <ControllerOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:roll-val is deprecated.  Use asctec_msgs-msg:roll instead.")
  (roll m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <ControllerOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:yaw-val is deprecated.  Use asctec_msgs-msg:yaw instead.")
  (yaw m))

(cl:ensure-generic-function 'thrust-val :lambda-list '(m))
(cl:defmethod thrust-val ((m <ControllerOutput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:thrust-val is deprecated.  Use asctec_msgs-msg:thrust instead.")
  (thrust m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControllerOutput>) ostream)
  "Serializes a message object of type '<ControllerOutput>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'nick)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'roll)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
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
  (cl:let* ((signed (cl:slot-value msg 'thrust)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControllerOutput>) istream)
  "Deserializes a message object of type '<ControllerOutput>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'nick) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'roll) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
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
      (cl:setf (cl:slot-value msg 'thrust) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControllerOutput>)))
  "Returns string type for a message object of type '<ControllerOutput>"
  "asctec_msgs/ControllerOutput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControllerOutput)))
  "Returns string type for a message object of type 'ControllerOutput"
  "asctec_msgs/ControllerOutput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControllerOutput>)))
  "Returns md5sum for a message object of type '<ControllerOutput>"
  "25c7094035da7c0bf36050e699ef0f7a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControllerOutput)))
  "Returns md5sum for a message object of type 'ControllerOutput"
  "25c7094035da7c0bf36050e699ef0f7a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControllerOutput>)))
  "Returns full string definition for message of type '<ControllerOutput>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%#attitude controller outputs; 0..200 = -100 .. +100 %~%int32 nick~%int32 roll~%int32 yaw~%~%#current thrust (height controller output); 0..200 = 0..100%~%int32 thrust~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControllerOutput)))
  "Returns full string definition for message of type 'ControllerOutput"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%#attitude controller outputs; 0..200 = -100 .. +100 %~%int32 nick~%int32 roll~%int32 yaw~%~%#current thrust (height controller output); 0..200 = 0..100%~%int32 thrust~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControllerOutput>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControllerOutput>))
  "Converts a ROS message object to a list"
  (cl:list 'ControllerOutput
    (cl:cons ':header (header msg))
    (cl:cons ':nick (nick msg))
    (cl:cons ':roll (roll msg))
    (cl:cons ':yaw (yaw msg))
    (cl:cons ':thrust (thrust msg))
))
