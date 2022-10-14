import cv2 as cv

img = cv.imread('Photos/images.jfif')
cv.imshow('Human', img)

cv.waitKey(0)