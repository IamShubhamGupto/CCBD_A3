# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:02:05 2020

@author: shubham_2
"""

import cv2
import numpy as np
img = cv2.imread(r'D:\SHUBHAM\CCBD\QGIS\BLR\BLR.63.tif')
h,w,c = img.shape
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_green = np.array([35,25,25])
upper_green = np.array([80,255,255])
mask = cv2.inRange(hsv, lower_green, upper_green)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
#res = cv2.bitwise_and(img,img, mask=mask)
#bi = cv2.
#print(mask.shape)
unique, counts = np.unique(mask, return_counts=True)
d = dict(zip(unique, counts))
print("d  = ",d)
'''
white_pixel = np.sum(mask == 255)
black_pixel = np.sum(mask == 0)
print("Number of white pixels = ",white_pixel)
print("Number of black pixels = ",black_pixel)
area = white_pixel/(white_pixel+black_pixel)
print("Area of white pixels = ",area)
'''