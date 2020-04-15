# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:02:05 2020

@author: shubham_2
"""

import cv2
import numpy as np
img = cv2.imread(r'D:\SHUBHAM\CCBD\tiles\blr_19_03.png')
h,w,c = img.shape
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_green = np.array([35,25,25])
upper_green = np.array([80,255,255])
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img,img, mask=mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
ret,threshold = cv2.threshold(res,1,255,cv2.THRESH_BINARY)
cv2.imshow('frame',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
white_pix = np.sum(threshold == 255)
print("Number of white pixels = ",white_pix)
area = white_pix/(h*w)
print("Area of white pixels = ",area)