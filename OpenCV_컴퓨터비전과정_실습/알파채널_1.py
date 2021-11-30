import cv2
import sys
#import numpy as np

src = cv2.imread('images/cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('images/rapa_logo.png', cv2.IMREAD_UNCHANGED)

mask = logo[:,:,3]
logo = logo[:,:,:-1]

h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w] 

cv2.copyTo(logo, mask, crop)

cv2.imshow("logo", logo)
cv2.imshow("mask", mask)
cv2.imshow("crop+", src)


cv2.waitKey(0)
cv2.destroyAllWindows()
