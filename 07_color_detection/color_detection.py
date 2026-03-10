import cv2
import os
from utils import getlimits
from PIL import Image

webCam = cv2.VideoCapture(0)
orange = [0, 165, 255]
while True:
    ret,frame = webCam.read()
    hsv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit=getlimits(orange)
    
    mask = cv2.inRange(hsv_image,lowerLimit,upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)

    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break


webCam.release()

cv2.destroyAllWindows()