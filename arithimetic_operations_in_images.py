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
cv2.waitKey(0)

print('max of 255 by cv2: {}'.format(cv2.add(np.uint8([200]),np.uint8([100]))))
print('min of 0 by cv2: {}'.format(cv2.subtract(np.uint8([50]),np.uint8([100]))))

print('wrap of max by np: {}'.format(np.uint8([200])+np.uint8([100])))
print('wrap of min by np: {}'.format(np.uint8([50])-np.uint8([100])))