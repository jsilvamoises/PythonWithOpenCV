# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:24:59 2019

@author: Usuario
"""

from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set the Path of image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
# Image Gray Scale
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Gaussian
blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Image",image)


# Simple Thresholding
(T,thresh) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh)

# Simple Thresholding InvBinary
(T,threshInv) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse",threshInv)

(T,thresh) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh)

cv2.imshow("Coins",cv2.bitwise_and(image,image, mask=threshInv))
cv2.waitKey(0)


# adaptative thresholding usin mean
thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("Threshold mean",thresh)

# adaptative thresholding using gaussian
thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("Threshold Gaussian",thresh)

cv2.waitKey(0)

