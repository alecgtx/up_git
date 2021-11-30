
import cv2
import mediapipe as mp
#from dynamikontrol import Module
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
tilt=125
pan=0
kit.servo[0].angle = pan
kit.servo[1].angle = tilt

cap= cv2.VideoCapture(0)
#x_medium = 0
#y_medium = 0

#PCA9685 = PCA9685.PCA9685
#pwm = PCA9685(0x40, debug=False)
#pwm.setPWMFreq(50)



ANGLE_STEP = 1

module = Module()

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
angle = 0 # motor current angle

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.flip(img, 1) # mirror image

    results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(img, detection)

            x1 = detection.location_data.relative_bounding_box.xmin # left side of face bounding box
            x2 = x1 + detection.location_data.relative_bounding_box.width # right side of face bounding box

            cx = (x1 + x2) / 2 # center of the face

            if cx < 0.4: # left -> clockwise
                angle += ANGLE_STEP
                module.motor.angle(angle)
            elif cx > 0.6: # right -> counter clockwise
                angle -= ANGLE_STEP
                module.motor.angle(angle)

            cv2.putText(img, '%d deg' % (angle), org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=255, thickness=2)

            break

    cv2.imshow('Face Cam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
face_detection.close()
module.disconnect()



#X_MAX = 2500.0
#X_MIN = 500.0
#X_HOME = 1500.0
# 
#Y_MAX = 2500.0
#Y_MIN = 500.0
#Y_HOME = 1500.0
#
#W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#fps = cap.get(cv2.CAP_PROP_FPS)
#print('W,H,fps: ', W , H , fps)
#
#def move(x_move, y_move):
#    pwm.setServoPulse(0,x_move)
#    pwm.setServoPulse(1,y_move)
#
#move(X_HOME, Y_HOME)
#
##初期位置
#now_degree_x, now_degree_y, move_degree_x, move_degree_y = X_HOME, Y_HOME, 0, 0
#
#while True:
#    _,  frame = cap.read()
#    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#    # red color
#    low_red  = np.array([161, 155, 84])
#    high_red = np.array([179, 255 ,255])
#    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
#
#    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
#
#    for cnt in contours:
#        (x, y, w, h) = cv2.boundingRect(cnt)
#
#        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#        x_medium = int((x + x + w) / 2)
#        y_medium = int((y + y + h) / 2)
#        
#        #640,480
#        move_degree_x = now_degree_x - (x_medium-320)*0.3
#        move_degree_y = now_degree_y - (y_medium-240)*0.3
#        
#        if move_degree_x > X_MIN and move_degree_x < X_MAX:
#            if move_degree_y > Y_MIN  and move_degree_y < Y_MAX:
#                move(move_degree_x, move_degree_y)
#                now_degree_x = move_degree_x
#                now_degree_y = move_degree_y
#        
#        #print(x_medium,y_medium)
#        break
#
#    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
#    cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 0), 2)
#    cv2.imshow("Frame", frame)
#    cv2.imshow("mask", red_mask)
#
#    key = cv2.waitKey(1)
#
#    if key == 27:
#        break
#
#cap.release()
#cv2.destoyALLWindows()