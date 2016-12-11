cmake_minimum_required(VERSION 2.8.3)
project(asctec_msgs)


find_package(catkin REQUIRED COMPONENTS
  std_msgs
  roscpp
  message_generation
)

add_message_files(
	FILES
	LLStatus.msg
	ControllerOutput.msg
	CtrlInput.msg
	CurrentWay.msg
	GPSDataAdvanced.msg
	GPSData.msg
	IMUCalcData.msg
	IMURawData.msg
	RCData.msg
	WaypointCommand.msg
	WaypointData.msg
)

generate_messages(
   DEPENDENCIES
   std_msgs
   roscpp
#   geometry_msgs
#   nav_msgs
#   std_msgs
)

catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES multiplanner_msgs
  CATKIN_DEPENDS message_runtime std_msgs roscpp
#  DEPENDS system_lib
)

include_directories( include
  ${catkin_INCLUDE_DIRS}
)
# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

#rosbuild_init()

#set the default path for built executables to the "bin" directory
#set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
#set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
#rosbuild_gensrv()

