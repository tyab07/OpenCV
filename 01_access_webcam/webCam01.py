import cv2

webCam = cv2.VideoCapture(0)

while True:
    ret,frame = webCam.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break



webCam.release()

cv2.destroyAllWindows()

