import cv2
import numpy as np

src = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('images/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

cv2.copyTo(src, mask, dst)

cv2.imshow("src", src)
cv2.imshow("mask", mask)
cv2.imshow("dst", dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
