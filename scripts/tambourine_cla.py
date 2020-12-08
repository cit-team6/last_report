#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler


class tambourine_text:
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    gripper = moveit_commander.MoveGroupCommander("gripper")

    ###
    ### グローバル宣言
    ###
    move_max_velocity_value = 0.5

    stop_time = 2.0  # 停止する時間を指定
    force_hold_stick = 0.5 # 棒を握る力を指定
    ### 縦
    tambourine_x_position_vertical = 0.043040 # タンバリンの手前のx座標を指定
    tambourine_y_position_vertical = 0.303386 # タンバリンのy座標を指定
    tambourine_z_position_vertical = 0.085469  # タンバリンの少し上のz座標を指定
    stick_angle_vertical = 1.3 # 棒の角度を指定

    """
    現在縦持ちで仮定しているためコメントアウト
    ### 横
    tambourine_x_position_horizontal = 0.005 # タンバリンの手前のx座標を指定
    tambourine_y_position_horizontal = 0.180 # タンバリンのy座標を指定
    tambourine_z_position_horizontal = 0.141 # タンバリンの少し上のz座標を指定
    stick_angle_horizontal = -3.14 * 9.0 / 10.0 # 棒の角度を指定
    """
    ###
    ### 変数宣言ここまで
    ###

    def main (self):
        ##rospy.init_node("crane_x7_pick_and_place_controller")

        self.robot = moveit_commander.RobotCommander()
        self.arm = moveit_commander.MoveGroupCommander("arm")
        self.gripper = moveit_commander.MoveGroupCommander("gripper")

        while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
            rospy.sleep(1.0)
        rospy.sleep(1.0)

        print("Group names:")
        print(self.robot.get_group_names())

        print("Current state:")
        print(self.robot.get_current_state())



        # アーム初期ポーズを表示
        arm_initial_pose = self.arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)
        """
        現在縦持ちで仮定しているためコメントアウト
        # 横持ち
    
        # タンバリンをたたくために位置移動
        def preparation_horizontal():
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = tambourine_x_position_horizontal 
            target_pose.position.y = tambourine_y_position_horizontal 
            target_pose.position.z = tambourine_z_position_horizontal 
            q = quaternion_from_euler(-3.14, 0, 3.14/2.0)  # 上方から掴みに行く場合
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            self.arm.set_pose_target(target_pose)  # 目標ポーズ設定
            self.arm.go()  # 実行
    
        # 角度を変化させタンバリンを叩く
        def hit_tambourine_horizontal():
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = tambourine_x_position_horizontal 
            target_pose.position.y = tambourine_y_position_horizontal 
            target_pose.position.z = tambourine_z_position_horizontal 
            q = quaternion_from_euler(stick_angle_horizontal, 0, 3.14/2.0)  # 上方から掴みに行く場合
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            self.arm.set_pose_target(target_pose)  # 目標ポーズ設定
            self.arm.go()  # 実行
        """
    
        # SRDFに定義されている"home"の姿勢にする
        self.arm.set_named_target("home")
        self.arm.go()
    
        #パターン-----縦持ち
    
        self.preparation_vertical()
        self.hit_tambourine_vertical()
        self.preparation_vertical()
        self.hit_tambourine_vertical()
        self.preparation_vertical()
        self.hit_tambourine_vertical()
        self.preparation_vertical()
        self.hit_tambourine_vertical()
        self.preparation_vertical()
        self.hit_tambourine_vertical()
        self.preparation_vertical()
        self.hit_tambourine_vertical()
    
        self.arm.set_max_velocity_scaling_factor(self.move_max_velocity_value)
        self.arm.set_named_target("home")
        self.arm.go()
    
        """
        現在縦持ちで仮定しているためコメントアウト
        #パターン-----横持ち
    
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
        self.preparation_horizontal()
        self.hit_tambourine_horizontal()
    
        self.arm.set_max_velocity_scaling_factor(self.move_max_velocity_value)
        self.arm.set_named_target("home")
        self.arm.go()
        """
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
        q = quaternion_from_euler(-3.14/2.0, 3.14, -3.14/2.0)  # 上方から掴みに行く場合
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  # 目標ポーズ設定
        self.arm.go()  # 実行

    # 縦持ち

    # タンバリンをたたくために位置移動
    def preparation_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.tambourine_x_position_vertical
        target_pose.position.y = self.tambourine_y_position_vertical
        target_pose.position.z = self.tambourine_z_position_vertical
        q = quaternion_from_euler(3.14 * 9 / 10, 3.14 / 2, -3.14)  # 上方から掴みに行く場合
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  # 目標ポーズ設定
        self.arm.go()  # 実行

    # 角度を変化させタンバリンを叩く
    def hit_tambourine_vertical(self):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = self.tambourine_x_position_vertical
        target_pose.position.y = self.tambourine_y_position_vertical
        target_pose.position.z = self.tambourine_z_position_vertical
        q = quaternion_from_euler(3.14 * 9 / 10, self.stick_angle_vertical, -3.14)  # 上方から掴みに行く場合
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        self.arm.set_pose_target(target_pose)  # 目標ポーズ設定
        self.arm.go()  # 実行
