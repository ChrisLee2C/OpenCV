import cv2 as cv

img = cv.imread('Photos/images.jfif')
cv.imshow('Human', img)

cv.waitKey(0)

capture = cv.VideoCapture('Videos/Video Of Funny Cat.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()