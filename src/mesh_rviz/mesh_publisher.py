import rospy
import rospkg
from visualization_msgs import msg

class MeshPublisher(object):
    """
    Class to publisher to show mesh object in Rviz
    """
    def run(name):
        rospy.init_node(name, anonymous=True)
        marker = msg.Marker()
        rospack = rospkg.RosPack()
        #self.configureMarker(marker, name)
        marker.header.frame_id = "map"
        #marker.type = msg.Marker.SPHERE
        marker.type = msg.Marker.MESH_RESOURCE
        marker.mesh_resource = rospack.get_path('mesh_rviz')+"/meshes/RGB_mesh.dae" 
        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 1
        marker.pose.position.y = 0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.color.r = 0.0
        marker.color.g = 0.5
        marker.color.b = 0.5
        marker.color.a = 1.0

        publisher = rospy.Publisher('mesh',msg.Marker, queue_size=1)
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            publisher.publish(marker)
            rate.sleep()


    
    def configureMarker(self, marker, name):
        marker.type = msg.Marker.MESH_RESOURCE
        marker.mesh_resource = "src/mesh_rviz/mesh_publisher.py" 
        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 1
        marker.pose.position.y = 0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.color.r = 0.0
        marker.color.g = 0.5
        marker.color.b = 0.5
        marker.color.a = 1.0
