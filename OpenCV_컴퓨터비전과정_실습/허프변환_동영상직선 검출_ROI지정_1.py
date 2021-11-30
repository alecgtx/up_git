import cv2
import sys
import numpy as np
import math

cap = cv2.VideoCapture('videos/road.mp4') 



while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape
    edges = cv2.Canny(frame, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160, minLineLength=100, maxLineGap=8)
    dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    vertices = np.array([[(200,h-70),(w/2+80, h/2+20),(w/2+150, h/2+20), (w-100,h-70)]], dtype=np.int32)
    mask = np.zeros_like(edges) # mask = img와 같은 크기의 빈 이미지
    if len(edges.shape) > 2: color = (255,255,255) # Color
    else: color = 255 # 흑백
    cv2.fillPoly(mask, vertices, color) #다각형부분(ROI 설정부분) color로 채움
    ROI_image = cv2.bitwise_and(edges, mask) # 이미지와 color로 채워진 ROI를 합침
    lines = cv.HoughLinesP(ROI_image, 1, np.pi / 180., 160, minLineLength=100, maxLineGap=5)
    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            cv.line(dst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

#
    cv2.imshow("Source", frame)
    cv2.imshow("ROI_image", ROI_image)
    cv2.imshow("dst", dst)    
#    cv2.imshow('src', frame)
    

    if cv2.waitKey(10) == 27: break




cv2.destroyAllWindows()