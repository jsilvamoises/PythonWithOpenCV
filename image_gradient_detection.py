# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:22:32 2019

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

iap = cv2.Laplacian(image,cv2.CV_64F)
iap = np.uint8(np.absolute(iap))

cv2.imshow("Laplace",iap)
cv2.waitKey(0)

sobelX = cv2.Sobel(image,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))


sobelCombined = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("Sobel X",sobelX)
cv2.imshow("Sobel Y",sobelY)
cv2.imshow("Sobel Combined",sobelCombined)

cv2.waitKey(0)





