# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:32:36 2019

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

rotated = imutils.rotate(image,90)
cv2.imshow("Rotated by 180 degrees",rotated)

cv2.waitKey(0)