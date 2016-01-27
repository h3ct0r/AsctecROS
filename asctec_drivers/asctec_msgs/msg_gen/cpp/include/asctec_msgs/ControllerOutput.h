/* Auto-generated by genmsg_cpp for file /opt/ros/groovy/share/asctec_drivers/asctec_msgs/msg/ControllerOutput.msg */
#ifndef ASCTEC_MSGS_MESSAGE_CONTROLLEROUTPUT_H
#define ASCTEC_MSGS_MESSAGE_CONTROLLEROUTPUT_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"

namespace asctec_msgs
{
template <class ContainerAllocator>
struct ControllerOutput_ {
  typedef ControllerOutput_<ContainerAllocator> Type;

  ControllerOutput_()
  : header()
  , nick(0)
  , roll(0)
  , yaw(0)
  , thrust(0)
  {
  }

  ControllerOutput_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , nick(0)
  , roll(0)
  , yaw(0)
  , thrust(0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef int32_t _nick_type;
  int32_t nick;

  typedef int32_t _roll_type;
  int32_t roll;

  typedef int32_t _yaw_type;
  int32_t yaw;

  typedef int32_t _thrust_type;
  int32_t thrust;


  typedef boost::shared_ptr< ::asctec_msgs::ControllerOutput_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::asctec_msgs::ControllerOutput_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ControllerOutput
typedef  ::asctec_msgs::ControllerOutput_<std::allocator<void> > ControllerOutput;

typedef boost::shared_ptr< ::asctec_msgs::ControllerOutput> ControllerOutputPtr;
typedef boost::shared_ptr< ::asctec_msgs::ControllerOutput const> ControllerOutputConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::asctec_msgs::ControllerOutput_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::asctec_msgs::ControllerOutput_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace asctec_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::asctec_msgs::ControllerOutput_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::asctec_msgs::ControllerOutput_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::asctec_msgs::ControllerOutput_<ContainerAllocator> > {
  static const char* value() 
  {
    return "25c7094035da7c0bf36050e699ef0f7a";
  }

  static const char* value(const  ::asctec_msgs::ControllerOutput_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x25c7094035da7c0bULL;
  static const uint64_t static_value2 = 0xf36050e699ef0f7aULL;
};

template<class ContainerAllocator>
struct DataType< ::asctec_msgs::ControllerOutput_<ContainerAllocator> > {
  static const char* value() 
  {
    return "asctec_msgs/ControllerOutput";
  }

  static const char* value(const  ::asctec_msgs::ControllerOutput_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::asctec_msgs::ControllerOutput_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# Software License Agreement (BSD License)\n\
#\n\
# Copyright (c) 2010\n\
#  William Morris <morris@ee.ccny.cuny.edu>\n\
#  Ivan Dryanovski <ivan.dryanovski@gmail.com>\n\
# All rights reserved.\n\
#\n\
# Redistribution and use in source and binary forms, with or without\n\
# modification, are permitted provided that the following conditions\n\
# are met:\n\
#\n\
#  * Redistributions of source code must retain the above copyright\n\
#    notice, this list of conditions and the following disclaimer.\n\
#  * Redistributions in binary form must reproduce the above\n\
#    copyright notice, this list of conditions and the following\n\
#    disclaimer in the documentation and/or other materials provided\n\
#    with the distribution.\n\
#  * Neither the name of CCNY Robotics Lab nor the names of its\n\
#    contributors may be used to endorse or promote products derived\n\
#    from this software without specific prior written permission.\n\
#\n\
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n\
# \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n\
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS\n\
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE\n\
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,\n\
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,\n\
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n\
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER\n\
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT\n\
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN\n\
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE\n\
# POSSIBILITY OF SUCH DAMAGE.\n\
\n\
Header header\n\
#attitude controller outputs; 0..200 = -100 .. +100 %\n\
int32 nick\n\
int32 roll\n\
int32 yaw\n\
\n\
#current thrust (height controller output); 0..200 = 0..100%\n\
int32 thrust\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::asctec_msgs::ControllerOutput_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::asctec_msgs::ControllerOutput_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::asctec_msgs::ControllerOutput_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::asctec_msgs::ControllerOutput_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.nick);
    stream.next(m.roll);
    stream.next(m.yaw);
    stream.next(m.thrust);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ControllerOutput_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::asctec_msgs::ControllerOutput_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::asctec_msgs::ControllerOutput_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "nick: ";
    Printer<int32_t>::stream(s, indent + "  ", v.nick);
    s << indent << "roll: ";
    Printer<int32_t>::stream(s, indent + "  ", v.roll);
    s << indent << "yaw: ";
    Printer<int32_t>::stream(s, indent + "  ", v.yaw);
    s << indent << "thrust: ";
    Printer<int32_t>::stream(s, indent + "  ", v.thrust);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ASCTEC_MSGS_MESSAGE_CONTROLLEROUTPUT_H

