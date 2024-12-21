#!/usr/bin/env python

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from nav_core.base_global_planner import BaseGlobalPlanner

class MyGlobalPlanner(BaseGlobalPlanner):
    def __init__(self):
        super(MyGlobalPlanner, self).__init__()
        # Initialize any variables or parameters for your planner

    def make_plan(self, start, goal, tolerance):
        # Implement your algorithm for generating a global plan here
        # The start and goal arguments are PoseStamped messages
        # The tolerance argument is a float that specifies the desired tolerance for the goal position

        # Create a Path message to store the global plan
        path_msg = Path()
        path_msg.header.frame_id = "map"

        # Add each waypoint as a PoseStamped message to the Path message
        # Example code for generating a straight-line path from start to goal:
        pose_start = PoseStamped()
        pose_start.header.frame_id = "map"
        pose_start.pose = start.pose
        path_msg.poses.append(pose_start)

        pose_goal = PoseStamped()
        pose_goal.header.frame_id = "map"
        pose_goal.pose = goal.pose
        path_msg.poses.append(pose_goal)

        return path_msg

def main():
    rospy.init_node('my_global_planner')

    # Create an instance of your custom global planner
    my_planner = MyGlobalPlanner()

    # Register your planner as a plugin with the ROS Navigation Stack
    rospy.loginfo("Registering MyGlobalPlanner as a plugin...")
    rospy.set_param('my_global_planner', 'my_package.MyGlobalPlanner')
    rospy.set_param('move_base/base_global_planner', 'my_global_planner/MyGlobalPlanner')

    rospy.spin()

if __name__ == '__main__':
    main()
