# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:28:49 2019

@author: Usuario
"""

import numpy as np
import cv2

rectangle = np.zeros((300,300),dtype="uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Rectangle",rectangle)

circle = np.zeros((300,300),dtype="uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("Circle",circle)


bitwisedAnd = cv2.bitwise_and(rectangle,circle)
cv2.imshow("BitwiredAnd",bitwisedAnd)

bitwisedOr = cv2.bitwise_or(circle,rectangle)
cv2.imshow("BitwiredOR",bitwisedOr)

bitwisedXOR = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("BitwiredOR",bitwisedXOR)

bitwisedNOT = cv2.bitwise_not(rectangle,circle)
cv2.imshow("BitwiredNOT",bitwisedNOT)

cv2.waitKey(0)