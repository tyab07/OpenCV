import cv2
import os

img = cv2.imread(os.path.join('.','dogs.jpeg'))

k_size = 9
image_blur = cv2.blur(img,(k_size,k_size))
cv2.imshow('original',img)
cv2.imshow('blur',image_blur)

cv2.waitKey(0)