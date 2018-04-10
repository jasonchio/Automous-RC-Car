#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time
from rrb2 import *

rr = RRB2()
def callback(data):

	if float(data.data) > 300:
                print float(data.data)

		rospy.loginfo(rospy.get_caller_id() + "forward ok")
		rr.set_motors(0.9,1,1.0,1) #forward left
		time.sleep(.5)
		rr.set_motors(.9,0,.9,1) #forward right
		time.sleep(.5)
		rr.set_motors(0,0,0,0) #stop
		time.sleep(.2)
		#rr.set_motors(.9,0,.9,1)
		#time.sleep(.2)
		#rr.set_motors(.9,1,.9,1)
		#time.sleep(.2)
		#rr.set_motors(0,0,0,0)

	#elif float(data.data) < 200:
	#	rospy.loginfo(rospy.get_caller_id() + "overflow")
	#	rr.set_motors(.9,0,.9,1)
	#	time.sleep(.2)

	else:
		rospy.loginfo(rospy.get_caller_id() + "EVADE")
		rr.set_motors(1.0,0,1.0,00) #go back right
		time.sleep(1)
		rr.set_motors(0,1,0,1) #stop
		time.sleep(.5)
		rr.set_motors(1.0,1,1.0,1) #go forward left
		time.sleep(1)
		print float(data.data)
		
	#if float(data.data) < 50:
	#	rospy.loginfo(rospy.get_caller_id() + "overflow")
	#	rr.set_motors(1.0,0,1.0,1) #go back left
	#	time.sleep(1)
	#	rr.set_motors(0,1,0,1) #stop
	#	time.sleep(.5)
	#	rr.set_motors(1.0,1,1.0,0) #go forward right
	#	time.sleep(1)
	#	print float(data.data)

		#rr.set_motors(1.0,1,.9,1)
		#rr.set_motors(0,0,.9,1)
		#rr.set_motors(0,0,.9,1)
		#time.sleep(1) 
 
	
def listener():

# In ROS, nodes are uniquely named. If two nodes with the same
# node are launched, the previous one is kicked off. The
# anonymous=True flag means that rospy will choose a unique
# name for our 'listener' node so that multiple listeners can
# run simultaneously.
	rospy.init_node('listener', anonymous=True, )
	rospy.Subscriber("chatter", String, callback,queue_size=1, buff_size = 2**24)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
if __name__ == '__main__':
	listener()
#Don't forget to make the node executable:
#chmod +x listener.py
