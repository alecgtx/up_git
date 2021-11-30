import cv2
import numpy as np

src = cv2.imread('images/lenna_noise.bmp')
dst = cv2.bilateralFilter(src, -1, 10, 1)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()





