# -*- coding: utf-8 -*-
"""
Sean Baker
Digital Image Processing
Project 1
2/8/22
"""

import numpy as np
import cv2
from PIL import Image


# Make 256x256 array full of 150 with data type uint8 for image1
image1 = np.full((256,256),150, dtype=('uint8'))
cv2.namedWindow('Image1')
cv2.imshow('Image1',image1)



# Make 256x256 empty uint8 array for image2
image2 = np.empty((256,256),dtype=('uint8'))

# Populate image2 array with vertical gradient
for x in range (0,256):
    image2[x] = x
cv2.namedWindow('Image2')
cv2.imshow('Image2',image2)



# Make 256x256 empty uint8 array for image3
image3 = np.empty((256,256),dtype=('uint8'))

# Populate image3 array with horizontal gradient
for y in range (0,256):
    for x in range (0,256):
        image3[x][y] = y
cv2.namedWindow('Image3')
cv2.imshow('Image3',image3)



# Make 256x256 empty uint8 array for image4
image4 = np.empty((256,256),dtype=('uint8'))

# Populate image4 array with diagonal gradient
# Using average of row and column
for y in range (0,256):
    for x in range (0,256):
        image4[x][y] = int((x + y)/2)
cv2.namedWindow('Image4')
cv2.imshow('Image4',image4)



# Make 256x256 empty uint8 array for image5
# and flipped copys of image4
image5 = np.empty((512,512),dtype=('uint8'))
image4yflip = np.flip(image4, axis=0)
image4xflip = np.flip(image4, axis=1)
image4bothflip = np.flip(image4xflip, axis=0)

# Populate each quadrant with flipped copies
for y in range (0,256):
    for x in range (0,256):
        image5[x][y] = image4[x][y]
        image5[x + 256][y] = image4yflip[x][y]
        image5[x][y + 256] = image4xflip[x][y]
        image5[x + 256][y + 256] = image4bothflip[x][y]
cv2.namedWindow('Image5')
cv2.imshow('Image5',image5)



# Load in lena_color.png to image and convert
# to grayscale.
path = r'lena_color.jpg'
preimage6 = cv2.imread(path)
image6 = cv2.cvtColor(preimage6, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Image6')
cv2.imshow('Image6',image6)



# 512x512 array for image7
# Create 3 mirrors of image6 and
# assign them to a quadrant of image7
image6yflip = np.flip(image6, axis=0)
image6xflip = np.flip(image6, axis=1)
image6bothflip = np.flip(image6xflip, axis=0)
image7 = np.empty((512,512),dtype=('uint8'))
for y in range (0,256):
    for x in range (0,256):
        image7[x][y] = image6[x][y]
        image7[x + 256][y] = image6yflip[x][y]
        image7[x][y + 256] = image6xflip[x][y]
        image7[x + 256][y + 256] = image6bothflip[x][y]     
cv2.namedWindow('Image7')
cv2.imshow('Image7',image7)



# Save image4 to “homework1_4.jpg"
cv2.imwrite('homework1_4.jpg', image4)


#Save image5 to "homework1_5.gif"
im = Image.fromarray(image5)
im.save('homework1_5.gif')


# Save image7 to "homework1_7.pgm"
cv2.imwrite('homework1_7.pgm', image7)



# 256x256x3 array for image11
# Copy image 2, 3, and 4 into the
# 3 RGB channels
image11 = np.empty((256,256,3),dtype=('uint8'))
for y in range (0,256):
    for x in range (0,256):
        image11[x][y][2] = image2[x][y]
        image11[x][y][1] = image3[x][y]
        image11[x][y][0] = image4[x][y]
cv2.namedWindow('Image11')
cv2.imshow('Image11',image11)



# Save image11 as "homework1_11.ppm"
cv2.imwrite('homework1_11.ppm', image11)


# Store color version of Lena in image13
image13 = cv2.imread(path)
cv2.namedWindow('Image13')
cv2.imshow('Image13',image13)



# 512x512 array with mirrored copies of Lena
# in each quadrant
image14 = np.empty((512,512,3),dtype=('uint8'))
image13yflip = np.flip(image13, axis=0)
image13xflip = np.flip(image13, axis=1)
image13bothflip = np.flip(image13xflip, axis=0)
for z in range (0,3):
    for y in range (0,256):
        for x in range (0,256):
            image14[x][y][z] = image13[x][y][z]
            image14[x + 256][y][z] = image13yflip[x][y][z]
            image14[x][y + 256][z] = image13xflip[x][y][z]
            image14[x + 256][y + 256][z] = image13bothflip[x][y][z]     
cv2.namedWindow('Image14')
cv2.imshow('Image14',image14)


# Save image14 to "homework1_14. jpg"
cv2.imwrite('homework1_14.jpg', image14)



cv2.waitKey(0)
cv2.destroyAllWindows()