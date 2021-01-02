#! /usr/bin/env python
import tambourine_cla
import manekin_cla
import cut_cla
import rospy
from std_msgs.msg import Int8

if __name__ == '__main__':
    pattern = 1
    tu = tambourine_cla.tambourine_text()
    tk = manekin_cla.manekin_txt()
    t2 = cut_cla.cut_txt()
    rospy.init_node('arm_controll_maneger', anonymous=True)
    #rospy.Subscriber("opencv_pruebacolor1", Int8, callback)
    while True :
        sum = 0
        n = 0
        while n < 20:
            if tu.run == False and tk.run == False:
                s = 0;
                s = rospy.wait_for_message("opencv_pruebacolor1", Int8)
                sum += 4*s.data            
                n +=1     
                print ("n=",n)
                print ("s = ",s.data)
        if sum / 20 <= 2:
            n = 0
            if pattern == 1:
                tu.run = True
                tu.main()
                pattern += 1
            elif pattern == 2:
                tk.run = True
                tk.main()
                pattern += 1
            elif pattern == 3:
                t2.run = True
                t2.main()
                pattern = 1               
        else:
            break
