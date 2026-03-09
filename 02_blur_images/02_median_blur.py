import os
import cv2

path = os.path.join('.','dogs.jpeg')
im = cv2.imread(path)
k_size = 9
img = cv2.medianBlur(im,k_size)
cv2.imshow('medianBlur',img)
cv2.waitKey(0)