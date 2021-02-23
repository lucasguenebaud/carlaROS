#!/usr/bin/env python

#Gets ego position, future trajectory
#Computes the best cockpit state to reach required position
#Publishes cockpit state

#>>> input : 
#LocOutput pose
#LocOutput destination
#spatialite map

#>>> output :
#LocOutput pose

import rospy
from std_msgs.msg import String
from carlaROSmsgs import LocOutput #TODO: make custom message LocOutput
from carlaROSmsgs import NavTraj #TODO: make custom message NavTraj
from carlaROSmsgs import CtrlState #TODO: make custom message CtrlState



loc = None
def new_loc(data):
    global loc
    loc = data

traj = None
def new_traj(data):
    global traj
    traj = data

def compute_state():
    return CtrlState()

def node():
    #init
    rospy.init_node('control', anonymous=True)
    #input
    rospy.Subscriber('loc_output', LocOutput, new_loc)
    rospy.Subscriber('nav_trajectory', NavTraj, new_traj)
    #output
    ctrl_cockpitstate = rospy.Publisher('ctrl_cockpitstate', CtrlState, queue_size=10)

    #loop
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cockpitstate = compute_state()
        rospy.loginfo(cockpitstate)
        ctrl_cockpitstate.publish(cockpitstate)
        rate.sleep()

if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
