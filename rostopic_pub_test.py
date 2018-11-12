#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool


def talker():
    pub = rospy.Publisher('chatter', Bool, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    hello_str = True
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        if hello_str is True:
            hello_str = False
        else:
            hello_str = True 
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
