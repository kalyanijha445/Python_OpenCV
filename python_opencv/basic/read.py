import cv2 as cv
# reading img
img = cv.imread('photos/cats.jpg')
cv.imshow('Cat', img)

# reading vdo
caputure = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = caputure.read()
    cv.imshow('video', frame)

    if cv. waitKey(20) & 0xFF==ord('d'):
        break
caputure.release()
cv.destroyAllWindows()
