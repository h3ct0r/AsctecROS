; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude CtrlInput.msg.html

(cl:defclass <CtrlInput> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (pitch
    :reader pitch
    :initarg :pitch
    :type cl:fixnum
    :initform 0)
   (roll
    :reader roll
    :initarg :roll
    :type cl:fixnum
    :initform 0)
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:fixnum
    :initform 0)
   (thrust
    :reader thrust
    :initarg :thrust
    :type cl:fixnum
    :initform 0)
   (ctrl
    :reader ctrl
    :initarg :ctrl
    :type cl:fixnum
    :initform 0)
   (chksum
    :reader chksum
    :initarg :chksum
    :type cl:fixnum
    :initform 0))
)

(cl:defclass CtrlInput (<CtrlInput>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CtrlInput>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CtrlInput)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<CtrlInput> is deprecated: use asctec_msgs-msg:CtrlInput instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'pitch-val :lambda-list '(m))
(cl:defmethod pitch-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:pitch-val is deprecated.  Use asctec_msgs-msg:pitch instead.")
  (pitch m))

(cl:ensure-generic-function 'roll-val :lambda-list '(m))
(cl:defmethod roll-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:roll-val is deprecated.  Use asctec_msgs-msg:roll instead.")
  (roll m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:yaw-val is deprecated.  Use asctec_msgs-msg:yaw instead.")
  (yaw m))

(cl:ensure-generic-function 'thrust-val :lambda-list '(m))
(cl:defmethod thrust-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:thrust-val is deprecated.  Use asctec_msgs-msg:thrust instead.")
  (thrust m))

(cl:ensure-generic-function 'ctrl-val :lambda-list '(m))
(cl:defmethod ctrl-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:ctrl-val is deprecated.  Use asctec_msgs-msg:ctrl instead.")
  (ctrl m))

(cl:ensure-generic-function 'chksum-val :lambda-list '(m))
(cl:defmethod chksum-val ((m <CtrlInput>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:chksum-val is deprecated.  Use asctec_msgs-msg:chksum instead.")
  (chksum m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CtrlInput>) ostream)
  "Serializes a message object of type '<CtrlInput>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'pitch)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'roll)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'yaw)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'thrust)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ctrl)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'chksum)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CtrlInput>) istream)
  "Deserializes a message object of type '<CtrlInput>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pitch) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'roll) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yaw) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'thrust) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ctrl) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'chksum) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CtrlInput>)))
  "Returns string type for a message object of type '<CtrlInput>"
  "asctec_msgs/CtrlInput")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CtrlInput)))
  "Returns string type for a message object of type 'CtrlInput"
  "asctec_msgs/CtrlInput")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CtrlInput>)))
  "Returns md5sum for a message object of type '<CtrlInput>"
  "6a2f3591afa7529005dcc3a5acd6e490")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CtrlInput)))
  "Returns md5sum for a message object of type 'CtrlInput"
  "6a2f3591afa7529005dcc3a5acd6e490")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CtrlInput>)))
  "Returns full string definition for message of type '<CtrlInput>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# serial command (=Scientific Interface)~%# Pitch input: -2047 .. 2047 (0 = neutral)~%int16 pitch~%# Roll input: -2047 .. 2047 (0 = neutral)~%int16 roll~%# R/C Stick input: -2047 .. 2047 (0 = neutral)~%int16 yaw~%# Collective: 0 .. 4095 (= 0 .. 100%)~%int16 thrust~%# control byte:~%#    bit 0: pitch control enabled~%#    bit 1: roll control enabled~%#    bit 2: yaw control enabled~%#    bit 3: thrust control enabled~%#  These bits can be used to only enable one axis at a time and thus to control~%#  the other axes manually. This usually helps a lot to set up and finetune~%#  controllers for each axis seperately.~%int16 ctrl~%int16 chksum~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CtrlInput)))
  "Returns full string definition for message of type 'CtrlInput"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# serial command (=Scientific Interface)~%# Pitch input: -2047 .. 2047 (0 = neutral)~%int16 pitch~%# Roll input: -2047 .. 2047 (0 = neutral)~%int16 roll~%# R/C Stick input: -2047 .. 2047 (0 = neutral)~%int16 yaw~%# Collective: 0 .. 4095 (= 0 .. 100%)~%int16 thrust~%# control byte:~%#    bit 0: pitch control enabled~%#    bit 1: roll control enabled~%#    bit 2: yaw control enabled~%#    bit 3: thrust control enabled~%#  These bits can be used to only enable one axis at a time and thus to control~%#  the other axes manually. This usually helps a lot to set up and finetune~%#  controllers for each axis seperately.~%int16 ctrl~%int16 chksum~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CtrlInput>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CtrlInput>))
  "Converts a ROS message object to a list"
  (cl:list 'CtrlInput
    (cl:cons ':header (header msg))
    (cl:cons ':pitch (pitch msg))
    (cl:cons ':roll (roll msg))
    (cl:cons ':yaw (yaw msg))
    (cl:cons ':thrust (thrust msg))
    (cl:cons ':ctrl (ctrl msg))
    (cl:cons ':chksum (chksum msg))
))
