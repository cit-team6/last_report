#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler

def main():
    rospy.init_node("joint_values_final")
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(1.0)
    gripper = moveit_commander.MoveGroupCommander("gripper")

    while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
        rospy.sleep(1.0)
    rospy.sleep(1.0)

    print("Group names:")
    print(robot.get_group_names())

    print("Current state:")
    print(robot.get_current_state())

    arm_x = 0.5
    arm_y = 0.5
    arm_z = 1.0

    # SRDFに定義されている"vertical"の姿勢にする
    # すべてのジョイントの目標角度が0度になる
    arm.set_named_target("vertical")
    arm.go()

    # 目標角度と実際の角度を確認
    print "joint_value_target (radians):"
    print arm.get_joint_value_target()
    print "current_joint_values (radians):"
    print arm.get_current_joint_values()

    # アーム初期ポーズを表示
    arm_initial_pose = arm.get_current_pose().pose
    print("Arm initial pose:")
    print(arm_initial_pose)

    #アーム開閉
    gripper.set_joint_value_target([0.1, 0.1])
    gripper.go()
    
    #マネキンまで移動
    def move():
        target_pose = geometry.msg.pose()
        target_pose.position.x = arm_x
        target_pose.position.y = arm_y
        target_pose.position.z = arm_z
        q = quaternion_from_euler( 0.0, 0.0, 0.0 )
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)
        arm.go()
    
    # SRDFに定義されている"home"の姿勢にする
    print("home")
    arm.set_named_target("home")
    arm.go()

    # SRDFに定義されている"vertical"の姿勢にする
    print("vertical")
    arm.set_named_target("vertical")
    arm.go()

    # 現在角度をベースに、目標角度を作成する
    target_joint_values = arm.get_current_joint_values()
    # 各ジョイントの角度を１つずつ変更する
    joint_angle = math.radians(-90)
    target_joint_values[2] = joint_angle

    arm.set_joint_value_target(target_joint_values)
    arm.go()
    print str(2) + "-> joint_value_target (degrees):",
    print math.degrees( arm.get_joint_value_target()[2] ),
    print ", current_joint_values (degrees):",
    print math.degrees( arm.get_current_joint_values()[2] )

    joint_angle = math.radians(-90)
    target_joint_values[3] = joint_angle
    arm.set_joint_value_target(target_joint_values)
    arm.go()

    joint_angle = math.radians(90)
    target_joint_values[2] = joint_angle
    arm.set_joint_value_target(target_joint_values)
    arm.go()

    rospy.sleep(3)
  
    # SRDFに定義されている"vertical"の姿勢にする
    print("vertical")
    arm.set_named_target("vertical")
    arm.go()   


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
