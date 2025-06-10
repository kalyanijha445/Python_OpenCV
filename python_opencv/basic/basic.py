import cv2 as cv

img = cv.imread('photos/park.jpg')
cv.imshow('park', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayimg', gray)

# blur an img
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blurimg', blur)
cv.waitKey(0)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edge', canny)

#  Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding(get back the same img)
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# croping
croped = img[50:200, 200:400]
cv.imshow('Cropped', croped)
cv.waitKey(0)