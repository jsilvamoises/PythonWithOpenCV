# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:53:36 2019
pip install pillow
pip install pytesseract
pip install tesseract
pip install tesseract-ocr

@author: Usuario
"""

from PIL import Image
import pytesseract

import argparse
import cv2
import os

# construct de argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required= True,help="Path to input image to OCR'd")
ap.add_argument("-p","--preprocess",type=str,default="thresh",help="Type of preprocessing to be done")
args = vars(ap.parse_args())

# --image: The path to the image we're sending through the OCR system
# --preprocess: The preprocessing


image = cv2.imread(args['image'])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args['preprocess'] == 'thresh':
    gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif args['preprocess'] == 'blur':
    gray = cv2.medianBlur(gray,3)
    
filename = "{}.png".format(str(os.getpid()))

cv2.imwrite(filename,gray)


# load the image as PIL/Pillow image.apply OCR and then delete the temporary file

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow("Image",image)
cv2.imshow("Output",gray)

cv2.waitKey(0)

