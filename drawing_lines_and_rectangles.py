# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:37:53 2019

@author: Usuario
"""

import numpy as np
import cv2

# define canvas of size 300x300 px, with 3 cannels (r,g,b)
canvas = np.zeros((300,300,3),dtype='uint8')

green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)

cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

cv2.line(canvas,(0,0),(300,300),red,3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)


cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)


cv2.rectangle(canvas,(16,16),(60,60),blue)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

