import cv2
#import sys
#import numpy as np


img = cv2.imread('images\cat_cat.jpg')



cv2.rectangle(img, (200, 40), (360, 195), (0, 255, 0), 1)
cv2.rectangle(img, (199, 20), (361, 39), (0, 128, 0), -1)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
