# import OpenCV python library
import cv2 as cv
import numpy as np
import sys

img = cv.imread('assets/messi.jpg',-1)

if img is None:
 sys.exit("Could not read the image.")

print(img)

print(type(img))


print(img.shape) # Height(No of Row), Width(No of Column) and Channel (represent color)
#OpenCV use BGR

# Blue     Green    Red
# [0-255]  [0-255]  [0-255]


#accessing 