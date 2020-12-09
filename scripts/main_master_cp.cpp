#include <iostream>
#include "ros/ros.h"
#include "std_msgs/Int8.h"

int n = 0;
void chatterCallback(const std_msgs::Int8& msg)
{
  n++;
  //ROS_INFO("subscribe: %d", msg.data.c_str());
  std::cout << "hello"<< n << std::endl;
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "main_master_co");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("opencv_pruebacolor1",2, chatterCallback);

  while(n<=100){
    ros::Rate(0.1);
    ros::spinOnce();
    std::cout << "ssssssss" << n << std::endl;
  }
  
  return 0;
}
