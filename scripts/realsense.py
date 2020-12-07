import rospy
from sensor_msgs.msg import Image

# Import OpenCV libraries and tools
#!/usr/bin/env python2.7
  # Import ROS libraries and messages
import rospy
from sensor_msgs.msg import Image

import numpy as np

  # Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError

  # Print "Hello!" to terminal
print "Hello!"

  # Initialize the ROS Node named 'pruebacolor1', allow multiple nodes to be run with this name
rospy.init_node('opencv_pruebacolor1', anonymous=True)

  # Print "Hello ROS!" to the Terminal and to a ROS Log file located in ~/.ros/log/loghash/*.log
rospy.loginfo("Hello ROS!")

  # Initialize the CvBridge class
bridge = CvBridge()

#Funcion vacia
def f(a):
	pass


  # Define a function to show the image in an OpenCV Window
def show_image(img):
	cv2.imshow("Image Window", img)
	cv2.waitKey(3)

  # Define a callback for the Image message
def image_callback(img_msg):
	# log some info about the image topic
	rospy.loginfo(img_msg.header)

	# Try to convert the ROS Image message to a CV2 Image
	try:
		cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
	except CvBridgeError, e:
		rospy.logerr("CvBridge Error: {0}".format(e))





#######################################################################################
	
	img = cv_image    #Imports the image 

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Opencv Uses BGR instead of RGB, so, to fix the color problem, we change the color channels

	img = cv2.resize(img,(400, 400)) #Resizes the image width and heioght

	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Makes the image gray


	faceCascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_eye.xml') #This program uses a xml cascade file, this files are trained with some data to recognize different things, in this case, face or eyes
	

	faces = faceCascade.detectMultiScale(imgGray,1.1,4) #Parameters to use for the face/eye recognition

	for(x,y,w,h) in faces: #Coordinates of the detected face
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  #Draws a rectangle in the defined coordinates
    	
	cv2.imshow("Result", img) #Shows the image with the rectangles


	cv2.waitKey(1) #This makes the program to run forever


###########################################################################################



      
  # Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)

  # Initialize an OpenCV Window named "Image Window"
#cv2.namedWindow("Image Window", 1)

  # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
	rospy.spin()
