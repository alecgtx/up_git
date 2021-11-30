import time
import cv2
import numpy as np


cap1 = cv2.VideoCapture('videos/video1.mp4')
cap2 = cv2.VideoCapture('videos/video2.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)
delay = round(100 / fps)
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#out = cv2.VideoWriter('1++2.avi', fourcc, fps, (w, h))

for i in range(frame_cnt1-effect_frames):
    ret1, frame1 = cap1.read()
    if not ret1:break

    cv2.imshow('video',frame1)
    if cv2.waitKey(delay)==27: break

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1 or not ret2:break

    dx = int(w * i / effect_frames)
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]
#    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(delay)==27:break

for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    if not ret2:break
#    out.write(frame2)
    cv2.imshow('frame', frame2)
    if cv2.waitKey(delay)==27:break  


cap1.release()
cap2.release()
cv2.destroyAllWindows()
