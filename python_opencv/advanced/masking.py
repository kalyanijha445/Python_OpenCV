#masking --> focus on certain part of img like focus on pepole faces apply masking & removing all the unwanted path of the img  
import cv2 as cv
import numpy as np

img = cv.imread('photos/cats 2.jpg')
cv.imshow('Cats', img)

# blank img are same size of img
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank_Image', blank)

# # circle_shape
mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (38,38), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird_shape', weird_shape)

# rectangle_box
mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 +100, img.shape[0]//2 +100), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird_shape-Masked img', masked)

cv.waitKey(0)