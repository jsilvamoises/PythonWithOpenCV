# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:02:51 2019

@author: Usuario
"""

import numpy as np
import cv2
from random import randint

# define canvas of size 300x300 px, with 3 cannels (r,g,b)
canvas = np.zeros((300,300,3),dtype='uint8')

green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)
white = (255,255,255)

# X Y radios
cv2.circle(canvas,(120,120),30,red,-1)
cv2.circle(canvas,(100,100),30,green,-1)
cv2.circle(canvas,(200,200),30,green,1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)


canvas = np.zeros((300,300,3),dtype='uint8')


(centerX,centerY) = (canvas.shape[1]//2,canvas.shape[0]//2)


def random_colors():
    return (randint(0, 255),randint(0, 255),randint(0, 255))

for r in range(0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,random_colors())
    
cv2.imshow("Concentrics Circles",canvas)
cv2.waitKey(0)

canvas = np.zeros((1024,2096,3),dtype='uint8')

for i in range(0,50):
    radius = np.random.randint(5,high=200)
    color = np.random.randint(5,high=256,size =(3,)).tolist()
    pt = np.random.randint(0,high = 2096,size =(2,))   
    cv2.circle(canvas,tuple(pt),radius,color,-1)
    
    
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
fileName = '%s.png'%randint(0,9999)
cv2.imwrite(fileName,canvas)
