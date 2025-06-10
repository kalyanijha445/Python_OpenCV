# contour --> boundary of objects , useful tools(when shape of object & img recognition)

import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank img', blank)

# BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Canny 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)


# another fxn threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold img', thresh)

contours, hirearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} Contour(s) found: ')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)

