import cv2
import sys
import numpy as np


oldx = oldy = -1
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        oldx, oldy = x, y
#        cv2.circle(img, (oldx, oldy), 10, (0, 0, 255), -1, cv2.LINE_AA)
        pts = np.array([[oldx, oldy], [oldx+100, oldy], [oldx+25, oldy+75], [oldx+50, oldy-25], [oldx+75, oldy+75]])
        cv2.polylines(img, [pts], True, (255, 0, 255), 2)

        cv2.imshow('image', img)
        
#img = np.ones((480, 640, 3), dtype=np.uint8) * 255
img=np.full((480,640,3),(255,255,255), dtype=np.uint8)

cv2.imshow('image', img)
cv2.setMouseCallback('image', on_mouse, img)
cv2.waitKey()




