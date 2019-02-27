# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:44:58 2019

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
cv2.imshow("Original Gray Scale Image",image)


cv2.waitKey(0)


eq = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization",np.hstack([image,eq]))

cv2.waitKey(0)
