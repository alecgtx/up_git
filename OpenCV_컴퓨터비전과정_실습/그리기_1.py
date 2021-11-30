import cv2
import sys
import numpy as np

img=np.full((480,480,3), 255, np.uint8)
cv2.line(img, (50, 50), (200, 100), (0, 255, 255), 2)
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
