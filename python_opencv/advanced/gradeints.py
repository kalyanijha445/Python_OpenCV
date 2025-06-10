# Gradients & edge detection
import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# laplaction
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel
soblex = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobley = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(soblex, sobley)

cv.imshow('sobel X', soblex)
cv.imshow('Sobel Y', sobley)
cv.imshow('Combined Sobel', combine_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)