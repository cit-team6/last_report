#! /usr/bin/env python
import tambourine_cla
import rospy

if __name__ == '__main__':
    tu = tambourine_cla.tambourine_text();
    try:
        if not rospy.is_shutdown():
            tu.main()
    except rospy.ROSInterruptException:
        pass
