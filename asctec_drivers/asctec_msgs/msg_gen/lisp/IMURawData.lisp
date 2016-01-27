; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude IMURawData.msg.html

(cl:defclass <IMURawData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (pressure
    :reader pressure
    :initarg :pressure
    :type cl:integer
    :initform 0)
   (gyro_x
    :reader gyro_x
    :initarg :gyro_x
    :type cl:fixnum
    :initform 0)
   (gyro_y
    :reader gyro_y
    :initarg :gyro_y
    :type cl:fixnum
    :initform 0)
   (gyro_z
    :reader gyro_z
    :initarg :gyro_z
    :type cl:fixnum
    :initform 0)
   (mag_x
    :reader mag_x
    :initarg :mag_x
    :type cl:fixnum
    :initform 0)
   (mag_y
    :reader mag_y
    :initarg :mag_y
    :type cl:fixnum
    :initform 0)
   (mag_z
    :reader mag_z
    :initarg :mag_z
    :type cl:fixnum
    :initform 0)
   (acc_x
    :reader acc_x
    :initarg :acc_x
    :type cl:fixnum
    :initform 0)
   (acc_y
    :reader acc_y
    :initarg :acc_y
    :type cl:fixnum
    :initform 0)
   (acc_z
    :reader acc_z
    :initarg :acc_z
    :type cl:fixnum
    :initform 0)
   (temp_gyro
    :reader temp_gyro
    :initarg :temp_gyro
    :type cl:fixnum
    :initform 0)
   (temp_ADC
    :reader temp_ADC
    :initarg :temp_ADC
    :type cl:integer
    :initform 0))
)

(cl:defclass IMURawData (<IMURawData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IMURawData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IMURawData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<IMURawData> is deprecated: use asctec_msgs-msg:IMURawData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:pressure-val is deprecated.  Use asctec_msgs-msg:pressure instead.")
  (pressure m))

(cl:ensure-generic-function 'gyro_x-val :lambda-list '(m))
(cl:defmethod gyro_x-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:gyro_x-val is deprecated.  Use asctec_msgs-msg:gyro_x instead.")
  (gyro_x m))

(cl:ensure-generic-function 'gyro_y-val :lambda-list '(m))
(cl:defmethod gyro_y-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:gyro_y-val is deprecated.  Use asctec_msgs-msg:gyro_y instead.")
  (gyro_y m))

(cl:ensure-generic-function 'gyro_z-val :lambda-list '(m))
(cl:defmethod gyro_z-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:gyro_z-val is deprecated.  Use asctec_msgs-msg:gyro_z instead.")
  (gyro_z m))

(cl:ensure-generic-function 'mag_x-val :lambda-list '(m))
(cl:defmethod mag_x-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:mag_x-val is deprecated.  Use asctec_msgs-msg:mag_x instead.")
  (mag_x m))

(cl:ensure-generic-function 'mag_y-val :lambda-list '(m))
(cl:defmethod mag_y-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:mag_y-val is deprecated.  Use asctec_msgs-msg:mag_y instead.")
  (mag_y m))

(cl:ensure-generic-function 'mag_z-val :lambda-list '(m))
(cl:defmethod mag_z-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:mag_z-val is deprecated.  Use asctec_msgs-msg:mag_z instead.")
  (mag_z m))

(cl:ensure-generic-function 'acc_x-val :lambda-list '(m))
(cl:defmethod acc_x-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_x-val is deprecated.  Use asctec_msgs-msg:acc_x instead.")
  (acc_x m))

(cl:ensure-generic-function 'acc_y-val :lambda-list '(m))
(cl:defmethod acc_y-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_y-val is deprecated.  Use asctec_msgs-msg:acc_y instead.")
  (acc_y m))

(cl:ensure-generic-function 'acc_z-val :lambda-list '(m))
(cl:defmethod acc_z-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_z-val is deprecated.  Use asctec_msgs-msg:acc_z instead.")
  (acc_z m))

(cl:ensure-generic-function 'temp_gyro-val :lambda-list '(m))
(cl:defmethod temp_gyro-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:temp_gyro-val is deprecated.  Use asctec_msgs-msg:temp_gyro instead.")
  (temp_gyro m))

(cl:ensure-generic-function 'temp_ADC-val :lambda-list '(m))
(cl:defmethod temp_ADC-val ((m <IMURawData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:temp_ADC-val is deprecated.  Use asctec_msgs-msg:temp_ADC instead.")
  (temp_ADC m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IMURawData>) ostream)
  "Serializes a message object of type '<IMURawData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'pressure)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'gyro_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'gyro_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'gyro_z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mag_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mag_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mag_z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'temp_gyro)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'temp_ADC)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IMURawData>) istream)
  "Deserializes a message object of type '<IMURawData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pressure) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gyro_x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gyro_y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gyro_z) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mag_x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mag_y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mag_z) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_z) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'temp_gyro) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'temp_ADC) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IMURawData>)))
  "Returns string type for a message object of type '<IMURawData>"
  "asctec_msgs/IMURawData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IMURawData)))
  "Returns string type for a message object of type 'IMURawData"
  "asctec_msgs/IMURawData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IMURawData>)))
  "Returns md5sum for a message object of type '<IMURawData>"
  "2cfd4b9ba0bc72be7f937c948d990cd9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IMURawData)))
  "Returns md5sum for a message object of type 'IMURawData"
  "2cfd4b9ba0bc72be7f937c948d990cd9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IMURawData>)))
  "Returns full string definition for message of type '<IMURawData>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%#pressure sensor 24-bit value, not scaled but bias free~%int32 pressure~%~%#16-bit gyro readings; 32768 = 2.5V~%int16 gyro_x~%int16 gyro_y~%int16 gyro_z~%~%#10-bit magnetic field sensor readings~%int16 mag_x~%int16 mag_y~%int16 mag_z~%~%#16-bit accelerometer readings~%int16 acc_x~%int16 acc_y~%int16 acc_z~%~%#16-bit temperature measurement using yaw-gyro internal sensor~%int16 temp_gyro~%~%#16-bit temperature measurement using ADC internal sensor~%int32 temp_ADC~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IMURawData)))
  "Returns full string definition for message of type 'IMURawData"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%#pressure sensor 24-bit value, not scaled but bias free~%int32 pressure~%~%#16-bit gyro readings; 32768 = 2.5V~%int16 gyro_x~%int16 gyro_y~%int16 gyro_z~%~%#10-bit magnetic field sensor readings~%int16 mag_x~%int16 mag_y~%int16 mag_z~%~%#16-bit accelerometer readings~%int16 acc_x~%int16 acc_y~%int16 acc_z~%~%#16-bit temperature measurement using yaw-gyro internal sensor~%int16 temp_gyro~%~%#16-bit temperature measurement using ADC internal sensor~%int32 temp_ADC~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IMURawData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     2
     2
     2
     2
     2
     2
     2
     2
     2
     2
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IMURawData>))
  "Converts a ROS message object to a list"
  (cl:list 'IMURawData
    (cl:cons ':header (header msg))
    (cl:cons ':pressure (pressure msg))
    (cl:cons ':gyro_x (gyro_x msg))
    (cl:cons ':gyro_y (gyro_y msg))
    (cl:cons ':gyro_z (gyro_z msg))
    (cl:cons ':mag_x (mag_x msg))
    (cl:cons ':mag_y (mag_y msg))
    (cl:cons ':mag_z (mag_z msg))
    (cl:cons ':acc_x (acc_x msg))
    (cl:cons ':acc_y (acc_y msg))
    (cl:cons ':acc_z (acc_z msg))
    (cl:cons ':temp_gyro (temp_gyro msg))
    (cl:cons ':temp_ADC (temp_ADC msg))
))
