# import os
import xml.etree.ElementTree as ET

class ConfigParser():
    """
    Parses the .xml file with the configs
        """

    def __init__(self, file_name):
        """
        Constructor

        """
        self._set_defaults()
        
        # self.cfgdir = os.path.dirname(os.path.realpath(cfgpath))
        tree = ET.parse(file_name)

        for files in tree.find('file_names'):
            if files.tag == "main_waypoint_files":
                self.main_waypoint_files = files.get('value')

            if files.tag == "backup_waypoint_files":
                self.backup_waypoint_files = files.get('value')

            if files.tag == "map_file_directory":
                self.map_file_directory = files.get('value')

        for params in tree.find('ros_params'):
            if params.tag == "hummingbird_name_param":
                self.hummingbird_name_param = params.get('value')

            if params.tag == "hummingbird_height_param":
                self.hummingbird_height_param = params.get('value')

            if params.tag == "hummingbird_velocity_param":
                self.hummingbird_velocity_param = params.get("value")

            if params.tag == "map_file_name_param":
                self.map_file_name_param = params.get("value")

            if params.tag == "plot_map_on_param":
                self.plot_map_on_param = params.get("value")

            if params.tag == "waypointList_size_param":
                self.waypointList_size_param = params.get("value")

            if params.tag == "waypoint_time_param":
                self.waypoint_time_param = params.get("value")

            if params.tag == "finishedWaypoints":
                self.finishedWaypoints = params.get("value")

            if params.tag == "external_base_name":
                self.external_base_name = params.get("value")

    def printXmlValues(self):
        print "main_waypoint_files: ", self.main_waypoint_files
        print "backup_waypoint_files: ", self.backup_waypoint_files
        print "map_file_directory: ", self.map_file_directory
        print "hummingbird_name: ", self.hummingbird_name_param
        print "hummingbird_height: ", self.hummingbird_height_param
        print "hummingbird_velocity: ", self.hummingbird_velocity_param
        print "map_file_name: ", self.map_file_name_param
        print "plot_map_on: ", self.plot_map_on_param
        print "waypointList_size_param: ", self.waypointList_size_param
        print "waypoint_time_param: ", self.waypoint_time_param
        print "finishedWaypoints: ", self.finishedWaypoints
        print "external_base_name: ", self.external_base_name

    def _set_defaults(self):
        self.main_waypoint_files = ""
        self.backup_waypoint_files = ""
        self.map_file_directory = ""
        self.hummingbird_name_param = ""
        self.hummingbird_height_param = ""
        self.hummingbird_velocity_param = ""
        self.map_file_name_param = ""
        self.plot_map_on_param = ""
        self.waypointList_size_param = ""
        self.waypoint_time_param = ""
        self.finishedWaypoints = ""
        self.external_base_name = ""


# Test whether xml parsing is working adequately
# cf = ConfigParser("/opt/ros/groovy/share/asctec_drivers/asctec_proc/scripts/asctec_drivers_config.xml").printXmlValues()
