import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.55):
    # Images videos live vdo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized_Image', resized_image)

# another capture method
def changeRes(width, height):
    # live vdo
    capture.set(3,width)
    capture.set(4,height)


# reading vdo
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv. waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
