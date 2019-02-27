# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:55:45 2019

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


gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray,(17,17),0)
cv2.imshow("Image",image)

canny = cv2.Canny(blurred,30,150)
cv2.imshow("Canny Edges detect",canny)


(cnts, _) = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("| count {} coins in this image".format(len(cnts)))

coins = image.copy()

cv2.drawContours(coins,cnts,-1,(0,255,0),2)
cv2.imshow("Coins",coins)

cv2.waitKey(0)