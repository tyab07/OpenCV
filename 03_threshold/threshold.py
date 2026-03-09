import cv2
import os

path = os.path.join('.','bear.jpeg')
img = cv2.imread(path)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
et,thresh = cv2.threshold(img_gray,100,300,cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('gray',img_gray)
cv2.imshow('Thesh',thresh)
cv2.waitKey(0)