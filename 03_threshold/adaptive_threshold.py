import cv2
import os

path = os.path.join('.','writing.jpeg')

img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
image = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,20)
cv2.imshow('img',img)
cv2.imshow('thresh',image)
cv2.waitKey(0)
