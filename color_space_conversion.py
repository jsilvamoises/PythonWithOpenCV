# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:35:49 2019

@author: Usuario
"""

import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set the Path of image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("LAV",lab)


cv2.waitKey(0)