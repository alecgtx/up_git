import cv2
import numpy as np

img1 = cv2.imread('images\cat.jpg')


img2=img1[1:400, 230:740]
img3=img1[1:400, 230:740].copy()

#img2.fill(0)

cv2.imshow("img1", img1)
#cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.moveWindow('img3', 500,500)

cv2.waitKey(0)
cv2.destroyAllWindows()
