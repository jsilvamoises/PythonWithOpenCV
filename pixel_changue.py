# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:38:06 2019

@author: Usuario
"""

from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set the Path of image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
"""

image = cv2.imread("C:/Users/Usuario/pictures/cat2.jpg")
image2 = cv2.imread("C:/Users/Usuario/Pictures/cat3.jpg")
image3 = cv2.imread("C:/Users/Usuario/Pictures/cat1.jpg")
(B,G,R) = cv2.split(image)
(B1,G1,R1) = cv2.split(image2)
(B2,G2,R2) = cv2.split(image3)

cv2.imshow("B",B)
cv2.imshow("G",G)
cv2.imshow("R",R)




merged = cv2.merge([R,G1,B2])
cv2.imshow("Merged",merged)
cv2.waitKey(0)

merged = cv2.merge([R1,G2,B])
cv2.imshow("Merged",merged)
cv2.waitKey(0)

merged = cv2.merge([R2,G2,B1])
cv2.imshow("Merged",merged)
cv2.waitKey(0)