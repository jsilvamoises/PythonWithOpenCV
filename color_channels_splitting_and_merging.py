# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:27:30 2019

@author: Usuario
"""

import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set the Path of image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])

(B,G,R) = cv2.split(image)

cv2.imshow("Red",R)
cv2.imshow("Blue",B)
cv2.imshow("Green",G)

cv2.waitKey(0)

# CONTINUAR DA SEÇÃO 20