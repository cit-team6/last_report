#! /usr/bin/env python
import tambourine_cla
import rospy
from std_msgs.msg import Int8

if __name__ == '__main__':
    #中村くんのクラスをインスタンス化
    tu = tambourine_cla.tambourine_text()
    
    rospy.init_node('arm_controll_maneger', anonymous=True)
    #rospy.Subscriber("opencv_pruebacolor1", Int8, callback)
    while True :
        sum = 0
        n = 0
        #２秒間のセンサーの値を平均化する
        while n < 20:
            if tu.run == False:
                s = 0;
                s = rospy.wait_for_message("opencv_pruebacolor1", Int8)
                sum += 4*s.data            
                n +=1     
                print ("n=",n)
                print ("s = ",s.data)
        #アームを動かす
        if sum / 20 <= 2:
            n = 0
            tu.run = True
            tu.main()
        else:
            break
