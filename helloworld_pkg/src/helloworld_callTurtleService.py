#! /usr/bin/env python

#import rospy library and the service msgs
from turtlesim.srv import *
import rospy
#wait until the service is available 
rospy.wait_for_service('turtle1/set_pen')
#create a callable proxy to a service
change_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)

#call the service and manage the exception if happends
try:
  resp1 = change_pen(0.5, 1,0,2,0)
except rospy.ServiceException as exc:
  print("Service did not process request: " + str(exc))
