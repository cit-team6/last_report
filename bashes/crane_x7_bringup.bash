#!/bin/bash
sudo chmod 666 /dev/ttyUSB0
roslaunch crane_x7_bringup demo.launch fake_execution:=false
