import time
import cv2
import numpy as np


cap1 = cv2.VideoCapture('videos/video1.mp4')
cap2 = cv2.VideoCapture('videos/video2.mp4')


 
while True: 
    ret, frame = cap1.read()
    if not ret: break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
cap1.release()
cv2.destroyAllWindows()

while True: 
    ret, frame = cap2.read()
    if not ret: break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
cap2.release()
cv2.destroyAllWindows()
