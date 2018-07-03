#! /usr/bin/env python
​import rospy                               # Import the Python library for ROS
from std_msgs.msg import Int32             # Import the Int32 message from the std_msgs package
​
rospy.init_node('helloworld_publisher')         # Initiate a Node named 'topic_publisher'
# Create a Publisher object, that will publish on the /counter topic
pub = rospy.Publisher('counter', Int32) #  messages of type Int32
​rate = rospy.Rate(0.2)                    # Set a publish rate of 2 Hz
count = Int32()                         # Create a var of type Int32
count.data = 0                          # Initialize 'count' variable
​
# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown(): 
	# Publish the message within the 'count' variable
	pub.publish(count)
  	count.data += 1                     # Increment 'count' variable
     rate.sleep()        # Make sure the publish rate maintains at 2 Hz
