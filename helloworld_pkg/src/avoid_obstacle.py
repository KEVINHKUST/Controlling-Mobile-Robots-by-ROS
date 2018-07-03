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
  
  #print len(msg.ranges)

  #If the distance to an obstacle in front of the robot is bigger than 1 meter, the robot will move forward
  if msg.ranges[front] > 1 and msg.ranges[frontleft]>1 and msg.ranges[frontleft]>1:
      move.linear.x = 0.2
      move.angular.z = 0.0

  else:
      #If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will turn left
      if msg.ranges[front] <= 1: 
         print "obstacle ahead, turning left" 
         move.linear.x = -0.5
         move.angular.z = 5.0
      #If the distance to an obstacle at the front-left side of the robot is smaller than 1 meters, the robot will turn right
      elif msg.ranges[frontleft] < 1:
         print "obstacle on the front-left, turning right" 
         move.linear.x = -0.2
         move.angular.z = -2
        
      #If the distance to an obstacle at the front-right side of the robot is smaller than 1 meters, the robot will turn left
      elif msg.ranges[frontright] < 1:
         print "obstacle on the front-right, turning left" 
         move.linear.x = -0.2
         move.angular.z = 2
  #If the distance to an obstacle at the left side of the robot is smaller than 0.4 meters, the robot will turn right
  if msg.ranges[left] < 0.4:
         print "obstacle on the left, turning right" 
         move.linear.x = 0.0
         move.angular.z = -1
        
   #If the distance to an obstacle at the right side of the robot is smaller than 0.4 meters, the robot will turn left
  if msg.ranges[right] < 0.4:
         print "obstacle on the right, turning left" 
         move.linear.x = 0.0
         move.angular.z = 1
  #print some info for debugging   
  print "vel",vel,"FL=",msg.ranges[frontleft],"F=",msg.ranges[front], "FR=",msg.ranges[frontright], "L=",msg.ranges[left],"R=",msg.ranges[right],"B=",msg.ranges[back]
   #publish the msg
  pub.publish(move)

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
