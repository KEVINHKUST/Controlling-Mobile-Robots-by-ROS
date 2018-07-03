#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(msg):
	print msg.linear, msg.angular
rospy.init_node("helloworld_subscriber")
sub = rospy.Subscriber('turtle1/cmd_vel',Twist, callback)
rospy.spin()

