import cv2


cap1 = cv2.VideoCapture('videos/woman.mp4') # 녹색 동영상
cap2 = cv2.VideoCapture('videos/raining.mp4') # 비오는 배경 동영상
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
# HSV 색 공간에서 녹색 영역을 검출하여 합성
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) #HSV:색상Hue 채도Saturation 명도Value
    mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
    cv2.copyTo(frame2, mask, frame1) #cv2.copyTo(src, mask, dst=None)
    cv2.imshow('frame', frame1) # 화면에 동영상 출력하기
    if cv2.waitKey(10) == 27: break

cap1.release()
cap2.release()
cv2.destroyAllWindows()


