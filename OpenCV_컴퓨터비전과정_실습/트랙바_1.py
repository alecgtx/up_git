import numpy as np
import cv2

def on_level_change(pos):
    value = pos * 8
    if value >= 255: #임계치 처리(saturation)
        value = 255
    img[:] = value
    cv2.imshow('image', img)
img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 32, on_level_change)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()


