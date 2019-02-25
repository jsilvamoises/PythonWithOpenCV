# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:49:09 2019

@author: Usuario
"""
import numpy as np
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set de path of image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)

resized = imutils.resize(image,30,40)
cv2.imshow("Resized 50",resized)

cv2.waitKey()