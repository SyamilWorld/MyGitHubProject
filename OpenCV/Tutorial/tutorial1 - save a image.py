# import OpenCV python library
import cv2 as cv
import sys

# read image file
# -1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It is the default flag.
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv.imread('assets/logo.png',-1)

# a check is executed, if the image was loaded correctly.
if img is None:
 sys.exit("Could not read the image.")

# resize image by pixel
#img = cv.resize(img,(400,500))


# resize image by percentage
img = cv.resize(img,(0,0), fx=0.2, fy=0.2)


# rotate image
#img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
#img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
img = cv.rotate(img, cv.ROTATE_180)


# show image
cv.imshow('Image', img)

# we want our window to be displayed until the user presses a key
k = cv.waitKey(0)


# the image is written to a file if the pressed key was the "s"-key
if k == ord("s"):

    #save image
    cv.imwrite('assets/new_img.png',img)


cv.destroyAllWindows()