import sys
import cv2

cap = cv2.VideoCapture(0)

file="photo.jpg"

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (200,90),(500,400),(255,255,255),3)
    cv2.imshow('result', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
    elif key == 13:
        img_frame=frame.copy()
        img_size=img_frame[90:400,270:480]
        cv2.imwrite(file, img_size)
        print(file, '저장됨')
