cmake_minimum_required(VERSION 2.8.3)
project(asctec_autopilot)

find_package(catkin REQUIRED COMPONENTS 
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  nodelet
  diagnostic_updater
  asctec_msgs
)


#generate_messages(
#  DEPENDENCIES
#  asctec_msgs
#)

catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES tp2
#  CATKIN_DEPENDS geometry_msgs nav_msgs roscpp rospy sensor_msgs std_msgs nodelet diagnostic_updater asctec_msgs
#  DEPENDS system_lib
)

include_directories( include
  ${catkin_INCLUDE_DIRS}
)

add_library(autopilot_nodelet src/autopilot_nodelet.cpp)
add_dependencies(autopilot_nodelet ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

#add_executable(autopilot_node src/autopilot_node.cpp)
#add_dependencies(autopilot_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
#target_link_libraries(autopilot_node autopilot_nodelet
#   ${catkin_LIBRARIES}
#)

add_executable(autopilot_node src/autopilot_node.cpp
                                src/autopilot.cpp
                                src/serial_interface.cpp
                                src/crc16.cpp 
                                src/telemetry.cpp)
add_dependencies(autopilot_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(autopilot_node autopilot_nodelet
   ${catkin_LIBRARIES}
)
