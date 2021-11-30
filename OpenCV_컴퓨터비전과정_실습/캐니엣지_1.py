import cv2
#import numpy as np

src = cv2.imread('images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.Canny(src, 50, 150)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()






