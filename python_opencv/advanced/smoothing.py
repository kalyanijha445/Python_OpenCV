# bluring img 
import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('CATS', img)

# method of bluring(Averaging)
average = cv.blur(img, (7,7))
cv.imshow('Averag_Blur', average)

# Gussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gussian_Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median_blur', median)

# Bilaterial Blur
bilaterial = cv.bilateralFilter(img, 10, 25, 25)
cv.imshow('Bilaterial_blur', bilaterial)

# use bilaterial & median blur
cv.waitKey(0)