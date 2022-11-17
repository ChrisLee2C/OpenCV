import cv2 as cv
import numpy as np

img = cv.imread('Photos/images.jfif')
cv.imshow('Human', img)

#translate image
def translate(img, x, y):
    # M = [1 0 x] 
    #     [0 1 y]
    transMat = np.float32([[1,0,x],[0,1,y]])
    #tuple of width and height
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> Left
# -y -> Up
#  x -> Right
#  y -> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

#rotate image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    #get rotation matrix by center, angle and scale
    #positive angle for anticlockwise, negative for clockwise
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimensions = (width,height)
    #Affine transform include translation, scaling and rotation
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#resize image
#AREA/DEFAULT for shrinking
#LINEAR/CUBIC for enlarging, CUBIC slower but better image
#a matter of preference
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flip image 0 for vertical, 1 for horizontal, -1 for both
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

#crop image again
crop = img[10:100, 20:200]
cv.imshow('Cropped', crop)

if ord('d'):
    cv.destroyAllWindows

cv.waitKey(0)