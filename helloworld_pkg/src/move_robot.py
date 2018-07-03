#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_rebot_node')
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1)
rate = rospy.Rate(100)
move_cmd = Twist()
#differential motion: Vx, OMEGAz
move_cmd.linear.x = 10
move_cmd.angular.z = 10

while not rospy.is_shutdown():
	pub.publish(move_cmd)
	rate.sleep()


