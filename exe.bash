#!/bin/bash
tab = "--tab-with-profile=roslaunch --command"
window = "--window-with-profile = roslaunch --command"
cd $HOME/catkin_ws/src/last_report/bashes
gnome-terminal --tab -e './roscore.bash' --tab -e './rs_camera.launch.bash' --tab -e './crane_x7_ros.launch.bash'
