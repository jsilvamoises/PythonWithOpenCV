# -*- coding: utf-8 -*-
import argparse
import cv2
from random import randint

# LOAD ARGS FROM PROMPT OR TERMINAL
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")

args = vars(ap.parse_args())

# LOAD IMAGE THIS IS IN ARGS
image = cv2.imread(args["image"])
# print(image)
print('width......: {} pixels '.format(image.shape[1]))
print('height.....: {} pixels '.format(image.shape[0]))
print('channels...: {}  '.format(image.shape[2]))

(b,g,r) = image[0,0] # column 0 line 0
print('Pixel at (0,0) - Red: {}, Greean: {}, Blue: {}'.format(r,g,b))

# CHANGE PIXEL COLOR
image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print('Pixel at (0,0) - Red: {}, Greean: {}, Blue: {}'.format(r,g,b))

# pixel region manipulation
corner = image[0:100,0:100]
cv2.imshow("Corner",corner)
cv2.waitKey(0)


image[0:100,0:100] =(0,255,0)
cv2.imshow("Updated",image)
cv2.waitKey(0)

image[0:255,0:255] = (125,123,122)
cv2.imshow("Updated 6",image)
cv2.waitKey(0)


image[0:255,0:255] = (125,123,122)
cv2.imshow("Updated 6",image)
cv2.waitKey(0)

image[0:255,0:255] = (randint(0, 255),randint(0, 255),randint(0, 255))
cv2.imshow("Updated Random",image)
cv2.waitKey(0)
