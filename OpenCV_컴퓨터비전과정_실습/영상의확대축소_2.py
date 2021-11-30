import cv2
#import numpy as np

src = cv2.imread('images/rose.bmp') # src.shape=(320, 480, 3)
dst1 = cv2.resize(src, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

