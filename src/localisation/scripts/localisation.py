#!/usr/bin/env python

#>>> input : 
#GPSFix gps_pos
#spatialie map #TODO

#>>> output :
#LocOutput pose

import rospy
from std_msgs.msg import String
from gps_common import GPSFix #TODO: fix import
from carlaROSmsgs import LocOutput #TODO: make custom message LocOutput

gps_pos = None

def new_gps_pos(data):
    global gps_pos
    gps_pos = data

def get_pose(pos):
    return pos

def node():
    #init
    rospy.init_node('localisation', anonymous=True)
    #input
    rospy.Subscriber('gps', GPSFix, new_gps_pos)
    #output
    loc_output = rospy.Publisher('loc_output', LocOutput, queue_size=10)

    #loop
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pose = get_pose(gps_pos)
        rospy.loginfo(pose)
        loc_output.publish(pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
