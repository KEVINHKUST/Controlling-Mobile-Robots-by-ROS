#!/usr/bin/env python

# import the required modules
import sys
import os
import rospy
# imports the AddTwoInts service 
from rospy_tutorials.srv import *
## add two numbers using the add_two_ints service
def add_two_ints_client(x, y):
    # It not necessary to call rospy.init_node() to make calls 
    # to a service. The service clients do not have to be nodes.
    # it is blocked until the add_two_ints service is available
    # a timeout can be specified    
    rospy.wait_for_service('add_two_ints')
    try:
        # create a handle to the add_two_ints service
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        print "Requesting %s+%s"%(x, y)
     
        # simplified style
        resp1 = add_two_ints(x, y)

        # formal style
        resp2 = add_two_ints.call(AddTwoIntsRequest(x, y))
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    
    argv = rospy.myargv()
    if len(argv) == 1:
        import random
        x = random.randint(-50000, 50000)
        y = random.randint(-50000, 50000)
   elif len(argv) == 3:
        try:
            x = int(argv[1])
            y = int(argv[2])
        except:
            print usage()
            sys.exit(1)
    else:
        print usage()
        sys.exit(1)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
