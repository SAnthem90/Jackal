import rospy
from geometry_msgs.msg import Twist
import time as t
from math import sqrt, pi, atan

rospy.init_node('turtlebot3_teleop')
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
turtlebot3_model = rospy.get_param("model", "burger")

x = float(input("Enter X : "))
y = float(input("Enter Y : "))
tr = sqrt(x * x + y * y)
an = atan(y/x)
an = 180 * an/pi
an = int(an/2.57)
tr = int(12.5*tr)

if x < 0:
    dt = -1
else:
    dt = 1

if y < 0:
    da = -1
else:
    da = 1

print(tr,an)

def angular():
    for i in range(abs(an)):
        twist = Twist()
        twist.angular.z = (da)*(0.5)
        t.sleep(0.1)
        pub.publish(twist)
def translation():
    for i in range(abs(tr)):
        twist = Twist()
        twist.linear.x = (dt)*(0.25)
        t.sleep(0.1)
        pub.publish(twist)

if x <0:
    translation()
    angular()
else:
    angular()
    translation()


