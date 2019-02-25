# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:20:38 2019

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

fliped = cv2.flip(image,1)
cv2.imshow("Flipped Horizontally",fliped)

fliped = cv2.flip(image,0)
cv2.imshow("Flipped Vertically",fliped)

fliped = cv2.flip(image,-1)
cv2.imshow("Flipped Both",fliped)

image = image*255
cv2.imshow("Combo",image)

cv2.waitKey()