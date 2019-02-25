# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:29:15 2019

@author: Usuario
"""

import argparse
import cv2
from random import randint
import numpy as np

# LOAD ARGS FROM PROMPT OR TERMINAL
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")

args = vars(ap.parse_args())

# LOAD IMAGE THIS IS IN ARGS
image = cv2.imread(args["image"])
cv2.imshow("Original",image)

M = np.ones(image.shape,dtype='uint8')*150
added = cv2.add(image,M)
cv2.imshow("Added",added)


M = np.ones(image.shape,dtype='uint8')*50
subtracted = cv2.subtract(image,M)
cv2.imshow("Subtracted",subtracted)


cv2.waitKey(0)