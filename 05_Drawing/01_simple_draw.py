import cv2
import os

path = os.path.join('.','board.jpeg')

img = cv2.imread(path)
print(img.shape)
#line
img = cv2.resize(img,(600,600))
cv2.line(img,(300,100),(500,300),(0,145,134),5)
#rectangle
cv2.rectangle(img,(100,200),(300,400),(123,232,100),7)
#circle
cv2.circle(img,(200,300),70,(234,234,123),7)

#text
cv2.putText(img,'circle',(160,300),cv2.FONT_HERSHEY_COMPLEX,1,(176,12,53),3)
cv2.imshow('Board',img)
cv2.waitKey(0)
