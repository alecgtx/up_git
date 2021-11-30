
import cv2
import sys
import mediapipe as mp
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
tilt=10
pan=90
kit.servo[0].angle = pan
kit.servo[1].angle = tilt

x_medium = 0
y_medium = 0

angle_step = 1
pTime = 0

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("Be sure Camera Connection!!!")
        break

    img = cv2.flip(img, 1) 
    results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(img, detection)

            x1 = detection.location_data.relative_bounding_box.xmin
            x2 = x1 + detection.location_data.relative_bounding_box.width 
            
            y1 = detection.location_data.relative_bounding_box.ymin 
            y2 = y1 + detection.location_data.relative_bounding_box.height

            x_medium = (x1 + x2) / 2 
            y_medium = (y1 + y2) / 2 
            print(x_medium, y_medium)
            print(pan, tilt)

            alpha_pan = 30 # gain
            if abs(x_medium - 0.5) > 0.05:
                pan  = pan + int((x_medium - 0.5) * alpha_pan) 
                if pan < 5:
                    pan = 5
                if pan > 175:
                    pan = 175      
                kit.servo[0].angle = pan
                #time.sleep(0.05)

            alpha_tilt = 30 # gain
            if abs(y_medium - 0.5) > 0.05:
                tilt  = tilt + int((0.5 - y_medium) * alpha_tilt) 
                if tilt < 5:
                    tilt = 5
                if tilt > 175:
                    tilt = 175      
                kit.servo[1].angle = tilt
                #time.sleep(0.05)          


            cv2.putText(img, 'Pan %d deg' % (pan), org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=255, thickness=2)
            cv2.putText(img, 'Tilt %d deg' % (tilt), org=(10, 60), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=255, thickness=2)
            break
    else:
        cv2.putText(img, 'Please in to the center of screen!' , org=(10, 150), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=255, thickness=2)
    
    cv2.imshow('Face Tracking Cam', img)
    if cv2.waitKey(1) == ord('q'):
        break

tilt=0
pan=90
kit.servo[0].angle = pan
time.sleep(0.05)
kit.servo[1].angle = tilt
time.sleep(0.05)

cap.release()
#face_detection.close()
cv2.destoyALLWindows()


