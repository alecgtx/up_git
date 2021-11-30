import time
import numpy as np
import cv2

cap = cv2.VideoCapture('videos/solidWhiteRight.mp4') # 비디오 열기
tm = cv2.TickMeter()
tm.reset()
tm.start()
t1 = time.time()
while True: 
    ret, frame = cap.read()
    if not ret:  # 리턴값 있는지 확인 필요
        print("---")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
tm.stop()
cap.release()

print('time:', (time.time() - t1))
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

cv2.destroyAllWindows()

