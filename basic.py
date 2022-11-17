import cv2 as cv

img = cv.imread('Photos/images.jfif')
cv.imshow('Human', img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur image inputting image, 2x2 kernel(must be odd and positive) 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#detect edge
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#dilate image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated',dilated)

#erode image 
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize image by width and height without concerning the aspect ratio
resize = cv.resize(img, (250,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#crop image by height and width
cropped = img[0:100, 0:200]
cv.imshow('Cropped', cropped)

if ord('d'):
    cv.destroyAllWindows

cv.waitKey(0)