#!/usr/bin/env pythonmail.com>
import rospy,copy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from pimouse_ros.msg import LightSensorValues

class WallStop():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

        self.sensors = LightSensorValues()
        rospy.Subscriber('/lightsensors', LightSensorValues, self.callback_sensors)

    def callback(self,messages):
        self.sensor_value = messages

    def run(self):
        rate = rospy.Rate(10)
        data = Twist()

        while not rospy.is_shutdown():
            data.linear.x = 0.2 if self.sensor_value.sum_all < 500 else 0.0
            self.cmd_vel.publish(data)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('wall_stop')
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off',Trigger).call)
    rospy.ServiceProxy('/motor_on',Trigger).call()
    WallStop().run()