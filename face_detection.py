# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:26:02 2019
pip install cmake
pip install face_recognition
@author: Usuario
"""

from PIL import Image
import face_recognition

# Load de jpg file into a numpy array
image = face_recognition.load_image_file("presidents.jpg")


# find all the faces in the image using the default HOG-based model
face_locations = face_recognition.face_locations(image)


print("I Found {} face(s) in this photograph.".format(len(face_locations)))


for face_location in face_locations:
    top,right,bottom,left = face_location
    print("A face is located at pixel location Top:{}, Left:{}, Bottom:{}, Right: {}\n".format(top,left,bottom,right))
    
    # access the actual face itself like this
    face_image = image[top:bottom,left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    
    
