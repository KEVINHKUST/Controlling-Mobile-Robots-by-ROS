#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
	print msg

rospy.init_node('read_robot_odom_node')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()

