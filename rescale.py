import cv2 as cv

#read image
img = cv.imread('Photos/images.jfif')
#show image
cv.imshow('Human', img)

#sth.shape returns a tuple of dimension, [0] for height and [1] for width
def rescaleFrame(frame, scale=0.75):
    #work on images,videos,live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image Resized', resized_image)

def changeRes(width,height):
    #work on live videos only (webcam,external camera)
    #propId -> video capture property ID,3 for width,4 for height
    capture.set(3,width)
    capture.set(4,height)

#read video frames
capture = cv.VideoCapture('Videos/Video Of Funny Cat.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
