import cv2
import mediapipe as mp

webCam = cv2.VideoCapture(0)

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selector=0, min_detection_confidence=0.5) as face_detection:

    while True:
        ret, frame = webCam.read()
        H, W, _ = frame.shape

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out = face_detection.process(img_rgb)

        if out.detections is not None:
            for detection in out.detections:

                bbox = detection.location_data.relative_bounding_box

                x1 = int(bbox.xmin * W)
                y1 = int(bbox.ymin * H)
                w = int(bbox.width * W)
                h = int(bbox.height * H)

                cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,255,0),2)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webCam.release()
cv2.destroyAllWindows()