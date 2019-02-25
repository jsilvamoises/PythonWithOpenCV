# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:01:34 2019

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

# shifted image down
shifted = imutils.translate(image,0,100)
cv2.imshow("Shifted down",shifted)

# shifted image up
shifted = imutils.translate(image,0,-100)
cv2.imshow("Shifted up",shifted)

# shifted image left
shifted = imutils.translate(image,-100,0)
cv2.imshow("Shifted left",shifted)

# shifted image right
shifted = imutils.translate(image,100,0)
cv2.imshow("Shifted right",shifted)


# shifted image right and down
shifted = imutils.translate(image,100,50)
cv2.imshow("Shifted right and down",shifted)



cv2.waitKey(0)



