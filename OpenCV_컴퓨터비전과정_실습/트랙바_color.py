import numpy as np
import cv2

def on_level_b(pos):  
    img[:,:,0] = pos
    cv2.imshow('image', img)
def on_level_g(pos):
    img[:,:,1] = pos
    cv2.imshow('image', img)
def on_level_r(pos):
    img[:,:,2] = pos
    cv2.imshow('image', img)

img = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('B', 'image', 0, 255, on_level_b)
cv2.createTrackbar('G', 'image', 0, 255, on_level_g)
cv2.createTrackbar('R', 'image', 0, 255, on_level_r)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()


