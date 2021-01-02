#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler

class cut_txt:
    arm = moveit_commander.MoveGroupCommander("arm")
    gripper = moveit_commander.MoveGroupCommander("gripper")
    stop_time = 2.0  # 停止する時間を指定
    force_hold_stick = 0.5 # 棒を握る力を指定
    te_x_position_vertical = 0.193040 # x
    te_y_position_vertical = -0.233386 # y
    te_z_position_vertical = 0.155469  # z
    stick_angle_vertical = 1.3 # 棒
    run = False
    def main(self):
        robot = moveit_commander.RobotCommander()
        

        while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
            rospy.sleep(1.0)
        rospy.sleep(1.0)

        print("Group names:")
        print(robot.get_group_names())

        print("Current state:")
        print(robot.get_current_state())



        

        # アーム初期ポーズを表示
        arm_initial_pose = self.arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)



        self.preparation_vertical()
        i = 0
        while i<2:
            i+=1
            self.preparation_vertical()
            self.p1_vertical()

        self.arm.set_max_velocity_scaling_factor(0.5)
        self.arm.set_named_target("home")
        self.arm.go()

        self.run = False
    # ハンドを開く/ 閉じる
    def move_gripper(self,pou):
        self.gripper.set_joint_value_target([pou, pou])
        self.gripper.go()

        # アームを移動する
    def move_arm(self,pos_x, pos_y, pos_z):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = pos_x
        target_pose.position.y = pos_y
        target_pose.position.z = pos_z
        q = quaternion_from_euler(-3.14/2.0, 3.14, -3.14/2.0) 
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  
        self.arm.go() 

    def preparation_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.te_x_position_vertical
        target_pose.position.y = self.te_y_position_vertical
        target_pose.position.z = self.te_z_position_vertical + 0.1
        q = quaternion_from_euler(0, 3.14, -0)  
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  
        self.arm.go()  

    def p1_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.te_x_position_vertical
        target_pose.position.y = self.te_y_position_vertical
        target_pose.position.z = self.te_z_position_vertical
        q = quaternion_from_euler(0, 3.14, -0)  
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  
        self.arm.go()  

    def p2_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.te_x_position_vertical
        target_pose.position.y = self.te_y_position_vertical
        target_pose.position.z = self.te_z_position_vertical
        q = quaternion_from_euler(0, 3.14, -3.14/2.0)  
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  
        self.arm.go()  

    def p3_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.te_x_position_vertical
        target_pose.position.y = self.te_y_position_vertical
        target_pose.position.z = self.te_z_position_vertical
        q = quaternion_from_euler(0, 3.14, -3.14/2.0) 
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose) 
        self.arm.go() 

    def p4_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.te_x_position_vertical
        target_pose.position.y = self.te_y_position_vertical
        target_pose.position.z = self.te_z_position_vertical
        q = quaternion_from_euler(0, 3.14, -3.14/2.0) 
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  
        self.arm.go() 