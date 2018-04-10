#!/usr/bin/env python
import cv2
import time
import rospy
import numpy as np
from std_msgs.msg import String

from rrb2 import *
import RPi.GPIO as GPIO


rr = RRB2()
lowerBound=np.array([33,80,40]) #Jason
upperBound=np.array([90,255,255])
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))
font = cv2.FONT_HERSHEY_SIMPLEX

def initCam():
	global camDown
	camDown = True

def callback(data):
	global camDown
	#print rr.get_distance()
#@	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


	if rr.get_distance() > 30:# and camDown:
		localtime = time.asctime( time.localtime(time.time()) )
		cap = cv2.VideoCapture(0)
		#out = cv2.VideoWriter(localtime + '.avi',cv2.cv.CV_FOURCC(*'XVID'), 20.0, (640,480))
		#camDown = False;
		#while float(data.data) < 100: 
		ret, frame = cap.read()
		width, height = tuple(frame.shape[1::-1])
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Jason
		#frame=cv2.resize(frame,(340,220))
		if ret==True:
		#	cv2.imshow("k" ,frame)
		#	cv2.waitKey(1)

		#Jason
		#img=cv2.resize(img,(340,220))

    	#convert BGR to HSV
    	#imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    	# create the Mask
			mask=cv2.inRange(hsv,lowerBound,upperBound)
    	#morphology
			maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
			maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

			maskFinal=maskClose
			conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
			bigwidth = 0
			x = 0
			w = 0 
			xx = 0
			yy = 0
			hh = 0
			#cv2.drawContours(frame,conts,-1,(255,0,0),3)
			for i in range(len(conts)):
		   		x,y,w,h=cv2.boundingRect(conts[i])
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255), 2)
        #cv2.cv.PutText(cv2.cv.fromarray(img), str(i+1),(x,y+h),font,(0,255,255))
    	#cv2.imshow("maskClose",maskClose)
    	#cv2.imshow("maskOpen",maskOpen)
    	#cv2.imshow("mask",mask)
			#cv2.imshow("cam",frame)
			#cv2.waitKey(10)
				if w > bigwidth:
					bigwidth = w
					xx = x
					yy = y
					hh = h
			
			
					
			distance = float(rr.get_distance())
			
			if x and (xx+ bigwidth/2 <= width/2):
				cv2.putText(frame,'GO LEFT',(100,100), font, 1,(0,0,255),2,cv2.CV_AA)
				rr.set_motors(1,0,.5,0) #forward left
			elif x and (xx+ bigwidth/2 > width/2): 
				cv2.putText(frame,'GO RIGHT',(100,100), font, 1,(0,0,255),2,cv2.CV_AA)
				rr.set_motors(1,0,.5,1) #forward right
				
			print distance
			if (distance <= 100.0): 
				cv2.putText(frame,'STOP',(100,100), font, 1,(0,0,255),2,cv2.CV_AA)
				rr.set_motors(0,0,0,0) #stop

						
				    
			cv2.imshow("cam",frame)
			cv2.waitKey(1)
			
#end of Jason
			#cv2.imwrite("/home/red1/catkin_ws/src/auto/photos/" + localtime + ".png",frame)
		

		# Release everything if job is finished
		#cap.release()
		#out.release()
		#camDown = True
	else:
		 rr.set_motors(0,0,0,0)
	 

def recordIfClose():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rate = rospy.Rate(.0001) 
	rate.sleep()
	rospy.spin() # spin() simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
	initCam()
	recordIfClose()


