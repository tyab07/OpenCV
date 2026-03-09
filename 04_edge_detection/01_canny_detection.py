import cv2
import os

path = os.path.join('.','player.jpeg')
img = cv2.imread(path)
edge_img = cv2.Canny(img,200,250)
cv2.imshow('Player',img)
cv2.imshow('Edge',edge_img)
cv2.waitKey(0)
