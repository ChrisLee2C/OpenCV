import cv2 as cv

img = cv.imread('Photos/images.jfif')
cv.imshow('Human', img)

#input 0 for wait forever
cv.waitKey(0)

capture = cv.VideoCapture('Videos/Video Of Funny Cat.mp4')

while True:
    #destruct into bool and frame
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    #waitfor 20 miliseconds and press d to close the window
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

#stops the video
capture.release()
#close the window
cv.destroyAllWindows()
