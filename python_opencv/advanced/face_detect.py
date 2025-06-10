# face detection using Haer Cascades 
import cv2 as cv

img = cv.imread('photos/group 1.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_person', gray)

haer_cascade = cv.CascadeClassifier('haer_face.xml')

faces_rect = haer_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected_faces', img)
cv.waitKey(0)