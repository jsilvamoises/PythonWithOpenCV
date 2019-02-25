# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:41:47 2019

@author: Usuario
"""

import numpy as np
import argparse
import cv2
import random


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Set de path of image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])


cv2.imshow("Original",image)

print(image.shape)

# crop de image startY 15 ,endY 222,startX:150,endX:400

cropped = image[15:222,150:400]

cv2.imshow("Cropped",cropped)

cv2.waitKey()

cv2.imwrite("cropped.png",cropped)


# image = np.zeros((300,300,3))
h,w =image.shape[:2]


def pixel_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

for i in range(100,h):#h
    for j in range(100,w):#w
        (r,g,b) = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print('R: {} G: {} B: {}'.format(r,g,b) )
        #image[i,j] = (r,g,b)
        image[i:j] = (r,g,b)
        
        
print('Fim')        
cv2.imshow("Cropped",image)
cv2.waitKey()

