#!/usr/bin/env python

import rospy
rospy.init_node('hello_loop')

print "hello world. This is my first ROS node"

rate = rospy.Rate(0.2)
while not rospy.is_shutdown():
    print "hello loop"

    rate.sleep()
