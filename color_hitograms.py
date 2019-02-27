# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:04:20 2019

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

# splist image int channels B,G,AND R
chans = cv2.split(image)

colors = ("#0091ea","#0097a7","#d32f2f")
plt.figure()
plt.title("Flattened color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color = color)
    plt.xlim([0,256])
           

plt.show()
   