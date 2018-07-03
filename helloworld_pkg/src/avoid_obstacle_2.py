#! /usr/bin/env python
# coding: utf-8
import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

vel=0

def callback_odom(msg_odom):
    global vel
    vel=(msg_odom.twist.twist.linear.x**2+msg_odom.twist.twist.linear.y**2) #raiz

def callback_laser(msg):
  left=90
  frontleft=30
  frontright=33
  right=270
  front=0
  back=180
  
  print len(msg.ranges)," ", msg.range_min

 

################### node main script  ############################
#node creation
rospy.init_node('avoid_obstacle_node')
#subscriber creation
laser_sub = rospy.Subscriber('/scan', LaserScan, callback_laser)
odom_sub = rospy.Subscriber('/odom', Odometry , callback_odom)#We subscribe to the laser's topic
#publisher creation
pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
move = Twist()

rospy.spin()
