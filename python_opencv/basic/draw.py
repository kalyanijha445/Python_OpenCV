import cv2  as cv
import numpy as np

# blank img
blank = np.zeros((500, 500,3), dtype='uint8')
cv.imshow('Blankiimg', blank)


# 1. paint the img  a certain color
blank[200:300, 300:400] = 0,0,255
cv.imshow('greemimg', blank)
cv.waitKey(0)

# 2.draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circleimg', blank)

# 4. draw a line
cv.line(blank, (0,0), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. write text
cv.putText(blank, 'Hello My name is kalyani', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)