#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image

import numpy as np

# Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError

#import rospy
from std_msgs.msg import Int8


#######################################################################################
eyes_size = 30
#######################################################################################

#Funcion vacia
def f(a):
 pass

def show_image(img):
 cv2.imshow("Image Window", img)
 cv2.waitKey(3)

###########################################################################################
def image_callback(img_msg):
 # log some info about the image topic
 rospy.loginfo(img_msg.header)

 # Try to convert the ROS Image message to a CV2 Image
 try:
  cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
 except CvBridgeError as e:
  rospy.logerr("CvBridge Error: {0}".format(e))
	
 img = cv_image    #Imports the image 

 img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Opencv Uses BGR instead of RGB, so, to fix the color problem, we change the color channels

 img = cv2.resize(img,(400, 400)) #Resizes the image width and heioght

 imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Makes the image gray

 eyesCascade = cv2.CascadeClassifier('/home/tougasakatani/catkin_ws/src/last_report/haarcascade_eye.xml') #This program uses a xml cascade file, this files are trained with some data to recognize different things, in this case, face or eyes
 facesCascade = cv2.CascadeClassifier('/home/tougasakatani/catkin_ws/src/last_report/haarcascade_frontalface_default.xml') #This program uses a xml cascade file, this files are trained with some data to recognize different things, in this case, face or eyes
 
 #eyes = eyesCascade.detectMultiScale(imgGray,1.1,4,minSize=(50, 50)) #Parameters to use for the face/eye recognition
 faces = facesCascade.detectMultiScale(imgGray,1.1,4,minSize=(100, 100))
 if len(faces) == 1:
  x,y,w,h= faces[0, :]
  cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
  eyes_gray = imgGray[y : y + int(h/2), x : x + w]
  eyes = eyesCascade.detectMultiScale(eyes_gray,1.1,4,minSize=(8, 8))
  if len(eyes) <=1:
   pub.publish(0)
  else:
   pub.publish(1)
   for ex, ey, ew, eh in eyes:
    cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 255, 0), 1)
 else:
   pub.publish(1)         
 
 """
 if len(eyes) >0:
  pub.publish(1)      
  for(x,y,w,h) in eyes:
   cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)       	   
 else:
  pub.publish(0)
 """

 cv2.imshow("Result", img)
 cv2.waitKey(1) #This makes the program to run forever
 
###########################################################################################
rospy.init_node('opencv_pruebacolor1', anonymous=1)

bridge = CvBridge()

pub = rospy.Publisher('opencv_pruebacolor1',Int8,queue_size = 1)



sub_image = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)

while not rospy.is_shutdown():
 rospy.spin()
