"""autogenerated by genpy from asctec_msgs/GPSDataAdvanced.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class GPSDataAdvanced(genpy.Message):
  _md5sum = "9ab56d8a7fca6e53fe5619fec119323d"
  _type = "asctec_msgs/GPSDataAdvanced"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Software License Agreement (BSD License)
#
# Copyright (c) 2010
#  William Morris <morris@ee.ccny.cuny.edu>
#  Ivan Dryanovski <ivan.dryanovski@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of CCNY Robotics Lab nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Header header
#latitude/longitude in deg * 10^7
int32 latitude
int32 longitude

#GPS height in mm
int32 height

#speed in x (E/W) and y(N/S) in mm/s
int32 speed_x
int32 speed_y

#GPS heading in deg * 100
int32 heading

#accuracy estimates in mm and mm/s
int32 horizontal_accuracy
int32 vertical_accuracy
int32 speed_accuracy

#number of satellite vehicles used in NAV solution
int32 numSV

#GPS status information; 0x03 = valid GPS fix
int32 status

#coordinates of current origin in deg * 10^7
int32 latitude_best_estimate
int32 longitude_best_estimate

#velocities in X (E/W) and Y (N/S) after data fusion
int32 speed_x_best_estimate
int32 speed_y_best_estimate

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','latitude','longitude','height','speed_x','speed_y','heading','horizontal_accuracy','vertical_accuracy','speed_accuracy','numSV','status','latitude_best_estimate','longitude_best_estimate','speed_x_best_estimate','speed_y_best_estimate']
  _slot_types = ['std_msgs/Header','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,latitude,longitude,height,speed_x,speed_y,heading,horizontal_accuracy,vertical_accuracy,speed_accuracy,numSV,status,latitude_best_estimate,longitude_best_estimate,speed_x_best_estimate,speed_y_best_estimate

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GPSDataAdvanced, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.latitude is None:
        self.latitude = 0
      if self.longitude is None:
        self.longitude = 0
      if self.height is None:
        self.height = 0
      if self.speed_x is None:
        self.speed_x = 0
      if self.speed_y is None:
        self.speed_y = 0
      if self.heading is None:
        self.heading = 0
      if self.horizontal_accuracy is None:
        self.horizontal_accuracy = 0
      if self.vertical_accuracy is None:
        self.vertical_accuracy = 0
      if self.speed_accuracy is None:
        self.speed_accuracy = 0
      if self.numSV is None:
        self.numSV = 0
      if self.status is None:
        self.status = 0
      if self.latitude_best_estimate is None:
        self.latitude_best_estimate = 0
      if self.longitude_best_estimate is None:
        self.longitude_best_estimate = 0
      if self.speed_x_best_estimate is None:
        self.speed_x_best_estimate = 0
      if self.speed_y_best_estimate is None:
        self.speed_y_best_estimate = 0
    else:
      self.header = std_msgs.msg.Header()
      self.latitude = 0
      self.longitude = 0
      self.height = 0
      self.speed_x = 0
      self.speed_y = 0
      self.heading = 0
      self.horizontal_accuracy = 0
      self.vertical_accuracy = 0
      self.speed_accuracy = 0
      self.numSV = 0
      self.status = 0
      self.latitude_best_estimate = 0
      self.longitude_best_estimate = 0
      self.speed_x_best_estimate = 0
      self.speed_y_best_estimate = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_15i.pack(_x.latitude, _x.longitude, _x.height, _x.speed_x, _x.speed_y, _x.heading, _x.horizontal_accuracy, _x.vertical_accuracy, _x.speed_accuracy, _x.numSV, _x.status, _x.latitude_best_estimate, _x.longitude_best_estimate, _x.speed_x_best_estimate, _x.speed_y_best_estimate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.latitude, _x.longitude, _x.height, _x.speed_x, _x.speed_y, _x.heading, _x.horizontal_accuracy, _x.vertical_accuracy, _x.speed_accuracy, _x.numSV, _x.status, _x.latitude_best_estimate, _x.longitude_best_estimate, _x.speed_x_best_estimate, _x.speed_y_best_estimate,) = _struct_15i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_15i.pack(_x.latitude, _x.longitude, _x.height, _x.speed_x, _x.speed_y, _x.heading, _x.horizontal_accuracy, _x.vertical_accuracy, _x.speed_accuracy, _x.numSV, _x.status, _x.latitude_best_estimate, _x.longitude_best_estimate, _x.speed_x_best_estimate, _x.speed_y_best_estimate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.latitude, _x.longitude, _x.height, _x.speed_x, _x.speed_y, _x.heading, _x.horizontal_accuracy, _x.vertical_accuracy, _x.speed_accuracy, _x.numSV, _x.status, _x.latitude_best_estimate, _x.longitude_best_estimate, _x.speed_x_best_estimate, _x.speed_y_best_estimate,) = _struct_15i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_15i = struct.Struct("<15i")
_struct_3I = struct.Struct("<3I")
