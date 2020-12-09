#! /usr/bin/env python
import tambourine_cla
import rospy
from std_msgs.msg import Int8

tu = tambourine_cla.tambourine_text()
#sub = rospy.Subscriber("opencv_pruebacolor1", Int8, callback)
sensor=[]
n = 0
Action_robot = False
def callback(jadge):
    global n
    global Action_robot
    sum = 0 
    #rospy.sleep(0.3)    
    if n >= 50:
        for i in sensor:
            sum += 2*i
        if sum / 50 < 1:
            print(sum / 10)
            Action_robot = True
        del sensor[:]
        #sub.shutdown()
        n = 0;
    else:
        print("jadge.data",jadge.data)
        print("n=",n)
        print("run=",tu.run)
        if tu.run == False :
            sensor.append(jadge.data)
            n+=1
tu = tambourine_cla.tambourine_text()
if __name__ == '__main__':
    rospy.init_node('arm_controll_maneger', anonymous=True)
    #rospy.Subscriber("opencv_pruebacolor1", Int8, callback)
    while n <= 50:
        if tu.run == False:
            s = 0;
            s = rospy.wait_for_message("opencv_pruebacolor1", Int8)
            if s.data == 1:
                n+=1     
            print ("n=",n)
            print ("s = ",s.data)
            print("SSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            #rospy.sleep(1)
            if n == 50:
                #Action_robot = False
                tu.run = True
                tu.main()      