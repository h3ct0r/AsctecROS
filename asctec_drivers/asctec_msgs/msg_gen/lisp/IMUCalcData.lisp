; Auto-generated. Do not edit!


(cl:in-package asctec_msgs-msg)


;//! \htmlinclude IMUCalcData.msg.html

(cl:defclass <IMUCalcData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (angle_nick
    :reader angle_nick
    :initarg :angle_nick
    :type cl:integer
    :initform 0)
   (angle_roll
    :reader angle_roll
    :initarg :angle_roll
    :type cl:integer
    :initform 0)
   (angle_yaw
    :reader angle_yaw
    :initarg :angle_yaw
    :type cl:integer
    :initform 0)
   (angvel_nick
    :reader angvel_nick
    :initarg :angvel_nick
    :type cl:integer
    :initform 0)
   (angvel_roll
    :reader angvel_roll
    :initarg :angvel_roll
    :type cl:integer
    :initform 0)
   (angvel_yaw
    :reader angvel_yaw
    :initarg :angvel_yaw
    :type cl:integer
    :initform 0)
   (acc_x_calib
    :reader acc_x_calib
    :initarg :acc_x_calib
    :type cl:fixnum
    :initform 0)
   (acc_y_calib
    :reader acc_y_calib
    :initarg :acc_y_calib
    :type cl:fixnum
    :initform 0)
   (acc_z_calib
    :reader acc_z_calib
    :initarg :acc_z_calib
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
   (acc_angle_nick
    :reader acc_angle_nick
    :initarg :acc_angle_nick
    :type cl:integer
    :initform 0)
   (acc_angle_roll
    :reader acc_angle_roll
    :initarg :acc_angle_roll
    :type cl:integer
    :initform 0)
   (acc_absolute_value
    :reader acc_absolute_value
    :initarg :acc_absolute_value
    :type cl:integer
    :initform 0)
   (Hx
    :reader Hx
    :initarg :Hx
    :type cl:integer
    :initform 0)
   (Hy
    :reader Hy
    :initarg :Hy
    :type cl:integer
    :initform 0)
   (Hz
    :reader Hz
    :initarg :Hz
    :type cl:integer
    :initform 0)
   (mag_heading
    :reader mag_heading
    :initarg :mag_heading
    :type cl:integer
    :initform 0)
   (speed_x
    :reader speed_x
    :initarg :speed_x
    :type cl:integer
    :initform 0)
   (speed_y
    :reader speed_y
    :initarg :speed_y
    :type cl:integer
    :initform 0)
   (speed_z
    :reader speed_z
    :initarg :speed_z
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0)
   (dheight
    :reader dheight
    :initarg :dheight
    :type cl:integer
    :initform 0)
   (dheight_reference
    :reader dheight_reference
    :initarg :dheight_reference
    :type cl:integer
    :initform 0)
   (height_reference
    :reader height_reference
    :initarg :height_reference
    :type cl:integer
    :initform 0))
)

(cl:defclass IMUCalcData (<IMUCalcData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IMUCalcData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IMUCalcData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asctec_msgs-msg:<IMUCalcData> is deprecated: use asctec_msgs-msg:IMUCalcData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:header-val is deprecated.  Use asctec_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'angle_nick-val :lambda-list '(m))
(cl:defmethod angle_nick-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:angle_nick-val is deprecated.  Use asctec_msgs-msg:angle_nick instead.")
  (angle_nick m))

(cl:ensure-generic-function 'angle_roll-val :lambda-list '(m))
(cl:defmethod angle_roll-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:angle_roll-val is deprecated.  Use asctec_msgs-msg:angle_roll instead.")
  (angle_roll m))

(cl:ensure-generic-function 'angle_yaw-val :lambda-list '(m))
(cl:defmethod angle_yaw-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:angle_yaw-val is deprecated.  Use asctec_msgs-msg:angle_yaw instead.")
  (angle_yaw m))

(cl:ensure-generic-function 'angvel_nick-val :lambda-list '(m))
(cl:defmethod angvel_nick-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:angvel_nick-val is deprecated.  Use asctec_msgs-msg:angvel_nick instead.")
  (angvel_nick m))

(cl:ensure-generic-function 'angvel_roll-val :lambda-list '(m))
(cl:defmethod angvel_roll-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:angvel_roll-val is deprecated.  Use asctec_msgs-msg:angvel_roll instead.")
  (angvel_roll m))

(cl:ensure-generic-function 'angvel_yaw-val :lambda-list '(m))
(cl:defmethod angvel_yaw-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:angvel_yaw-val is deprecated.  Use asctec_msgs-msg:angvel_yaw instead.")
  (angvel_yaw m))

(cl:ensure-generic-function 'acc_x_calib-val :lambda-list '(m))
(cl:defmethod acc_x_calib-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_x_calib-val is deprecated.  Use asctec_msgs-msg:acc_x_calib instead.")
  (acc_x_calib m))

(cl:ensure-generic-function 'acc_y_calib-val :lambda-list '(m))
(cl:defmethod acc_y_calib-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_y_calib-val is deprecated.  Use asctec_msgs-msg:acc_y_calib instead.")
  (acc_y_calib m))

(cl:ensure-generic-function 'acc_z_calib-val :lambda-list '(m))
(cl:defmethod acc_z_calib-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_z_calib-val is deprecated.  Use asctec_msgs-msg:acc_z_calib instead.")
  (acc_z_calib m))

(cl:ensure-generic-function 'acc_x-val :lambda-list '(m))
(cl:defmethod acc_x-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_x-val is deprecated.  Use asctec_msgs-msg:acc_x instead.")
  (acc_x m))

(cl:ensure-generic-function 'acc_y-val :lambda-list '(m))
(cl:defmethod acc_y-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_y-val is deprecated.  Use asctec_msgs-msg:acc_y instead.")
  (acc_y m))

(cl:ensure-generic-function 'acc_z-val :lambda-list '(m))
(cl:defmethod acc_z-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_z-val is deprecated.  Use asctec_msgs-msg:acc_z instead.")
  (acc_z m))

(cl:ensure-generic-function 'acc_angle_nick-val :lambda-list '(m))
(cl:defmethod acc_angle_nick-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_angle_nick-val is deprecated.  Use asctec_msgs-msg:acc_angle_nick instead.")
  (acc_angle_nick m))

(cl:ensure-generic-function 'acc_angle_roll-val :lambda-list '(m))
(cl:defmethod acc_angle_roll-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_angle_roll-val is deprecated.  Use asctec_msgs-msg:acc_angle_roll instead.")
  (acc_angle_roll m))

(cl:ensure-generic-function 'acc_absolute_value-val :lambda-list '(m))
(cl:defmethod acc_absolute_value-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:acc_absolute_value-val is deprecated.  Use asctec_msgs-msg:acc_absolute_value instead.")
  (acc_absolute_value m))

(cl:ensure-generic-function 'Hx-val :lambda-list '(m))
(cl:defmethod Hx-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:Hx-val is deprecated.  Use asctec_msgs-msg:Hx instead.")
  (Hx m))

(cl:ensure-generic-function 'Hy-val :lambda-list '(m))
(cl:defmethod Hy-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:Hy-val is deprecated.  Use asctec_msgs-msg:Hy instead.")
  (Hy m))

(cl:ensure-generic-function 'Hz-val :lambda-list '(m))
(cl:defmethod Hz-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:Hz-val is deprecated.  Use asctec_msgs-msg:Hz instead.")
  (Hz m))

(cl:ensure-generic-function 'mag_heading-val :lambda-list '(m))
(cl:defmethod mag_heading-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:mag_heading-val is deprecated.  Use asctec_msgs-msg:mag_heading instead.")
  (mag_heading m))

(cl:ensure-generic-function 'speed_x-val :lambda-list '(m))
(cl:defmethod speed_x-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:speed_x-val is deprecated.  Use asctec_msgs-msg:speed_x instead.")
  (speed_x m))

(cl:ensure-generic-function 'speed_y-val :lambda-list '(m))
(cl:defmethod speed_y-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:speed_y-val is deprecated.  Use asctec_msgs-msg:speed_y instead.")
  (speed_y m))

(cl:ensure-generic-function 'speed_z-val :lambda-list '(m))
(cl:defmethod speed_z-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:speed_z-val is deprecated.  Use asctec_msgs-msg:speed_z instead.")
  (speed_z m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:height-val is deprecated.  Use asctec_msgs-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'dheight-val :lambda-list '(m))
(cl:defmethod dheight-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:dheight-val is deprecated.  Use asctec_msgs-msg:dheight instead.")
  (dheight m))

(cl:ensure-generic-function 'dheight_reference-val :lambda-list '(m))
(cl:defmethod dheight_reference-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:dheight_reference-val is deprecated.  Use asctec_msgs-msg:dheight_reference instead.")
  (dheight_reference m))

(cl:ensure-generic-function 'height_reference-val :lambda-list '(m))
(cl:defmethod height_reference-val ((m <IMUCalcData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asctec_msgs-msg:height_reference-val is deprecated.  Use asctec_msgs-msg:height_reference instead.")
  (height_reference m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IMUCalcData>) ostream)
  "Serializes a message object of type '<IMUCalcData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'angle_nick)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'angle_roll)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'angle_yaw)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'angvel_nick)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'angvel_roll)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'angvel_yaw)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_x_calib)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_y_calib)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_z_calib)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
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
  (cl:let* ((signed (cl:slot-value msg 'acc_angle_nick)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_angle_roll)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'acc_absolute_value)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'Hx)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'Hy)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'Hz)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mag_heading)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'speed_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'speed_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'speed_z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
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
  (cl:let* ((signed (cl:slot-value msg 'dheight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'dheight_reference)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'height_reference)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IMUCalcData>) istream)
  "Deserializes a message object of type '<IMUCalcData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle_nick) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle_roll) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle_yaw) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angvel_nick) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angvel_roll) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angvel_yaw) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_x_calib) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_y_calib) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_z_calib) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
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
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_angle_nick) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_angle_roll) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'acc_absolute_value) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Hx) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Hy) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Hz) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mag_heading) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed_x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed_y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed_z) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dheight) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'dheight_reference) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height_reference) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IMUCalcData>)))
  "Returns string type for a message object of type '<IMUCalcData>"
  "asctec_msgs/IMUCalcData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IMUCalcData)))
  "Returns string type for a message object of type 'IMUCalcData"
  "asctec_msgs/IMUCalcData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IMUCalcData>)))
  "Returns md5sum for a message object of type '<IMUCalcData>"
  "69fa9ec7b73af705eabe7dcbfd39ac85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IMUCalcData)))
  "Returns md5sum for a message object of type 'IMUCalcData"
  "69fa9ec7b73af705eabe7dcbfd39ac85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IMUCalcData>)))
  "Returns full string definition for message of type '<IMUCalcData>"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# angles derived by integration of gyro_outputs, drift compensated by data fusion;~%#-90000..+90000 pitch(nick) and roll, 0..360000 yaw; 1000 = 1 degree~%~%int32 angle_nick~%int32 angle_roll~%int32 angle_yaw~%~%# angular velocities, raw values [16 bit], bias free, in 0.0154 degree/s (=> 64.8 = 1 degree/s)~%~%int32 angvel_nick~%int32 angvel_roll~%int32 angvel_yaw~%~%# acc-sensor outputs, calibrated: -10000..+10000 = -1g..+1g~%~%int16 acc_x_calib~%int16 acc_y_calib~%int16 acc_z_calib~%~%# horizontal / vertical accelerations: -10000..+10000 = -1g..+1g~%~%int16 acc_x~%int16 acc_y~%int16 acc_z~%~%# reference angles derived by accelerations only: -90000..+90000; 1000 = 1 degree~%~%int32 acc_angle_nick~%int32 acc_angle_roll~%~%# total acceleration measured (10000 = 1g)~%~%int32 acc_absolute_value~%~%# magnetic field sensors output, offset free and scaled; units not determined, ~%# as only the direction of the field vector is taken into account~%~%int32 Hx~%int32 Hy~%int32 Hz~%~%# compass reading: angle reference for angle_yaw: 0..360000; 1000 = 1 degree~%~%int32 mag_heading~%~%# pseudo speed measurements: integrated accelerations, pulled towards zero; units unknown;~%# used for short-term position stabilization~%~%int32 speed_x~%int32 speed_y~%int32 speed_z~%~%# height in mm (after data fusion)~%~%int32 height~%~%# diff. height in mm/s (after data fusion)~%~%int32 dheight~%~%# diff. height measured by the pressure sensor [mm/s]~%~%int32 dheight_reference~%~%# height measured by the pressure sensor [mm]~%~%int32 height_reference~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IMUCalcData)))
  "Returns full string definition for message of type 'IMUCalcData"
  (cl:format cl:nil "# Software License Agreement (BSD License)~%#~%# Copyright (c) 2010~%#  William Morris <morris@ee.ccny.cuny.edu>~%#  Ivan Dryanovski <ivan.dryanovski@gmail.com>~%# All rights reserved.~%#~%# Redistribution and use in source and binary forms, with or without~%# modification, are permitted provided that the following conditions~%# are met:~%#~%#  * Redistributions of source code must retain the above copyright~%#    notice, this list of conditions and the following disclaimer.~%#  * Redistributions in binary form must reproduce the above~%#    copyright notice, this list of conditions and the following~%#    disclaimer in the documentation and/or other materials provided~%#    with the distribution.~%#  * Neither the name of CCNY Robotics Lab nor the names of its~%#    contributors may be used to endorse or promote products derived~%#    from this software without specific prior written permission.~%#~%# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS~%# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT~%# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS~%# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE~%# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,~%# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,~%# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;~%# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER~%# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT~%# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN~%# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE~%# POSSIBILITY OF SUCH DAMAGE.~%~%Header header~%# angles derived by integration of gyro_outputs, drift compensated by data fusion;~%#-90000..+90000 pitch(nick) and roll, 0..360000 yaw; 1000 = 1 degree~%~%int32 angle_nick~%int32 angle_roll~%int32 angle_yaw~%~%# angular velocities, raw values [16 bit], bias free, in 0.0154 degree/s (=> 64.8 = 1 degree/s)~%~%int32 angvel_nick~%int32 angvel_roll~%int32 angvel_yaw~%~%# acc-sensor outputs, calibrated: -10000..+10000 = -1g..+1g~%~%int16 acc_x_calib~%int16 acc_y_calib~%int16 acc_z_calib~%~%# horizontal / vertical accelerations: -10000..+10000 = -1g..+1g~%~%int16 acc_x~%int16 acc_y~%int16 acc_z~%~%# reference angles derived by accelerations only: -90000..+90000; 1000 = 1 degree~%~%int32 acc_angle_nick~%int32 acc_angle_roll~%~%# total acceleration measured (10000 = 1g)~%~%int32 acc_absolute_value~%~%# magnetic field sensors output, offset free and scaled; units not determined, ~%# as only the direction of the field vector is taken into account~%~%int32 Hx~%int32 Hy~%int32 Hz~%~%# compass reading: angle reference for angle_yaw: 0..360000; 1000 = 1 degree~%~%int32 mag_heading~%~%# pseudo speed measurements: integrated accelerations, pulled towards zero; units unknown;~%# used for short-term position stabilization~%~%int32 speed_x~%int32 speed_y~%int32 speed_z~%~%# height in mm (after data fusion)~%~%int32 height~%~%# diff. height in mm/s (after data fusion)~%~%int32 dheight~%~%# diff. height measured by the pressure sensor [mm/s]~%~%int32 dheight_reference~%~%# height measured by the pressure sensor [mm]~%~%int32 height_reference~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IMUCalcData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     2
     2
     2
     2
     2
     2
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IMUCalcData>))
  "Converts a ROS message object to a list"
  (cl:list 'IMUCalcData
    (cl:cons ':header (header msg))
    (cl:cons ':angle_nick (angle_nick msg))
    (cl:cons ':angle_roll (angle_roll msg))
    (cl:cons ':angle_yaw (angle_yaw msg))
    (cl:cons ':angvel_nick (angvel_nick msg))
    (cl:cons ':angvel_roll (angvel_roll msg))
    (cl:cons ':angvel_yaw (angvel_yaw msg))
    (cl:cons ':acc_x_calib (acc_x_calib msg))
    (cl:cons ':acc_y_calib (acc_y_calib msg))
    (cl:cons ':acc_z_calib (acc_z_calib msg))
    (cl:cons ':acc_x (acc_x msg))
    (cl:cons ':acc_y (acc_y msg))
    (cl:cons ':acc_z (acc_z msg))
    (cl:cons ':acc_angle_nick (acc_angle_nick msg))
    (cl:cons ':acc_angle_roll (acc_angle_roll msg))
    (cl:cons ':acc_absolute_value (acc_absolute_value msg))
    (cl:cons ':Hx (Hx msg))
    (cl:cons ':Hy (Hy msg))
    (cl:cons ':Hz (Hz msg))
    (cl:cons ':mag_heading (mag_heading msg))
    (cl:cons ':speed_x (speed_x msg))
    (cl:cons ':speed_y (speed_y msg))
    (cl:cons ':speed_z (speed_z msg))
    (cl:cons ':height (height msg))
    (cl:cons ':dheight (dheight msg))
    (cl:cons ':dheight_reference (dheight_reference msg))
    (cl:cons ':height_reference (height_reference msg))
))
