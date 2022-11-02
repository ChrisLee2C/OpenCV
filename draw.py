import cv2 as cv
import numpy as np

#height, width, number of color channels
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
img = cv.imread('Photos/images.jfif')
cv.imshow('Human', img)

#Paint the image a certain color R-G-B
#top to down, left to right [height,width]
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

#draw rectangle img, starting pt, ending pt, color, thickness cv.FILLED -> -1
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), 
    (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#draw circle img, centre, radius, color, thickness
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 250//2, (0,255,0),  thickness=2)
cv.imshow('Circle', blank)

#draw line img, starting pt, ending pt, color, thickness
cv.line(blank, (0,0), (500,500), (255,0,0), thickness=2)
cv.imshow('Line', blank)

#write text
cv.putText(blank, 'Hello, my name is Chris', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)