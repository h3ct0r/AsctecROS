; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude RCData.msg.html

(cl:defclass <RCData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (channels_in
    :reader channels_in
    :initarg :channels_in
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 8 :element-type 'cl:fixnum :initial-element 0))
   (channels_out
    :reader channels_out
    :initarg :channels_out
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 8 :element-type 'cl:fixnum :initial-element 0))
   (lock
    :reader lock
    :initarg :lock
    :type cl:fixnum
    :initform 0))
)

(cl:defclass RCData (<RCData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RCData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RCData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<RCData> is deprecated: use asctec_msgs-msg:RCData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <RCData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'channels_in-val :lambda-list '(m))
(cl:defmethod channels_in-val ((m <RCData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:channels_in-val is deprecated.  Use asctec_msgs-msg:channels_in instead.")
  (channels_in m))

(cl:ensure-generic-function 'channels_out-val :lambda-list '(m))
(cl:defmethod channels_out-val ((m <RCData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:channels_out-val is deprecated.  Use asctec_msgs-msg:channels_out instead.")
  (channels_out m))

(cl:ensure-generic-function 'lock-val :lambda-list '(m))
(cl:defmethod lock-val ((m <RCData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:lock-val is deprecated.  Use asctec_msgs-msg:lock instead.")
  (lock m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RCData>) ostream)
  "Serializes a message object of type '<RCData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'channels_in))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'channels_out))
  (cl:let* ((signed (cl:slot-value msg 'lock)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RCData>) istream)
  "Deserializes a message object of type '<RCData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:setf (cl:slot-value msg 'channels_in) (cl:make-array 8))
  (cl:let ((vals (cl:slot-value msg 'channels_in)))
    (cl:dotimes (i 8)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  (cl:setf (cl:slot-value msg 'channels_out) (cl:make-array 8))
  (cl:let ((vals (cl:slot-value msg 'channels_out)))
    (cl:dotimes (i 8)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'lock) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RCData>)))
  "Returns string type for a message object of type '<RCData>"
  "asctec_msgs/RCData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RCData)))
  "Returns string type for a message object of type 'RCData"
  "asctec_msgs/RCData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RCData>)))
  "Returns md5sum for a message object of type '<RCData>"
  "d486363e6033911606202acafb1bc1a0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RCData)))
  "Returns md5sum for a message object of type 'RCData"
  "d486363e6033911606202acafb1bc1a0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RCData>)))
  "Returns full string definition for message of type '<RCData>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%#    struct RC_DATA~%#    {~%#      //channels as read from R/C receiver~%#      unsigned short channels_in[8];~%#      //channels bias free, remapped and scaled to 0..4095~%#      unsigned short channels_out[8];~%#     //Indicator for valid R/C receiption~%#      unsigned char lock;~%#    };~%Header header~%# channels as read from R/C receiver~%int16[8] channels_in~%~%#channels bias free, remapped and scaled to 0..4095~%int16[8] channels_out~%~%#indicator for valid R/C receiption~%int16 lock~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RCData)))
  "Returns full string definition for message of type 'RCData"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%#    struct RC_DATA~%#    {~%#      //channels as read from R/C receiver~%#      unsigned short channels_in[8];~%#      //channels bias free, remapped and scaled to 0..4095~%#      unsigned short channels_out[8];~%#     //Indicator for valid R/C receiption~%#      unsigned char lock;~%#    };~%Header header~%# channels as read from R/C receiver~%int16[8] channels_in~%~%#channels bias free, remapped and scaled to 0..4095~%int16[8] channels_out~%~%#indicator for valid R/C receiption~%int16 lock~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RCData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'channels_in) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'channels_out) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RCData>))
  "Converts a ROS message object to a list"
  (cl:list 'RCData
    (cl:cons ':header (header msg))
    (cl:cons ':channels_in (channels_in msg))
    (cl:cons ':channels_out (channels_out msg))
    (cl:cons ':lock (lock msg))
))
