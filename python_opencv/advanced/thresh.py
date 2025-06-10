# Threshholding --> Binarization of img  
import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple threshholding --> manually specify threshhold value
threshold , thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple_Thresholded', thresh)

threshold , thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple_Thresholded _Inverse', thresh_inv)

# Adaptive Thresholding --> computing optimal threshhold value  basis of mean & gussian opencv calculate
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshholding', adaptive_thresh)

# thresh_inv
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Threshholding', adaptive_thresh)

# gussian
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Threshholding', adaptive_thresh)


cv.waitKey(0)