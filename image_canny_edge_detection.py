# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:45:29 2019

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


image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blurred",image)

canny = cv2.Canny(image,30,150)
cv2.imshow("Canny",canny)
cv2.waitKey(0)