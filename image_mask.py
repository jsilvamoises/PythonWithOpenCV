# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:55:15 2019

@author: Usuario
"""
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set the Path of image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

# using mask
mask = np.zeros(image.shape[:2],dtype="uint8")
(cX,cY) = (image.shape[1]//2,image.shape[0]//2) # Center of image
cv2.rectangle(mask,(cX-75,cY-75),(cX+75,cY+75),255,-1)
cv2.imshow("Mask",mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Mask Apllied to Image",masked)
cv2.waitKey(0)

# Using Circle Mask
mask_circle = np.zeros(image.shape[:2],dtype="uint8")
(cX,cY) = (image.shape[1]//2,image.shape[0]//2)
cv2.circle(mask_circle,(cX,cY),100,255,-1)
cv2.imshow("Circle Mask",mask_circle)

masked_circle = cv2.bitwise_and(image,image,mask=mask_circle)
cv2.imshow("Mask Circle Apllied to Image",masked_circle)

cv2.waitKey(0)
