#! /usr/bin/env python
import tambourine_cla
import rospy
from std_msgs.msg import Int8

tu = tambourine_cla.tambourine_text()
sensor=[]
n = 0 
def callback(jadge):
    global n
    sum = 0    
    if n >= 20:
        for i in sensor:
            sum += i
        if sum / 10 < 1:
            print(sum / 10)
            tu.main()
        del sensor[:]
        n=0
    else:
        print(jadge.data)
        sensor.append(jadge.data)
        n+=1
    
    """
    if not rospy.is_shutdown():
        if jadge.data == False:
            tu.main()
        else:
            pass
    """
    """
    try:
        
    except rospy.ROSInterruptException:
        pass
    """

if __name__ == '__main__':
    rospy.init_node('arm_controll_maneger', anonymous=True)
    rospy.Subscriber("opencv_pruebacolor1", Int8, callback)
    rospy.spin()
    
