# bitwise operators --> use for img procesing  like masks
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# basic bitwise operator
#  1.Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_And',bitwise_and)

# 2.Bitwise OR --> intersecting & non-intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_Or', bitwise_or)

# 3.Bitwise Xor --> non-intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_Xor', bitwise_xor)

# Biwise Not --> converted black to white & vice versa
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise_Not', bitwise_not)
cv.waitKey(0)