#!/usr/bin/env python

#Gets ego position, arrival destination, map
#Plans graph_trajectory through map
#Plans future way points trajectory to next gate
#Publishes way points trajectory

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


loc = None
def new_loc(data):
    global loc
    loc = data

# destination = None #TODO: service for that
# def new_destination(data):
#     global destination
#     destination = data

# def compute_gates():
#     return []

# def make_traj(pose,next_gate):
#     return []

# gates = None
def compute_traj(pose):
    # global gates
    # if gates is None:
    #     gates = compute_gates()
    # next_gate = gates.pop()
    # traj = make_traj(pose,next_gate)
    traj = [pose for _ in range(30)]
    return traj

def node():
    #init
    rospy.init_node('navigation', anonymous=True)
    #input
    rospy.Subscriber('loc_output', LocOutput, new_loc)
    #output
    nav_trajectory = rospy.Publisher('nav_trajectory', NavTraj, queue_size=10)

    #loop
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        traj = compute_traj(loc['pose'])
        rospy.loginfo(traj)
        nav_trajectory.publish(traj)
        rate.sleep()

if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
