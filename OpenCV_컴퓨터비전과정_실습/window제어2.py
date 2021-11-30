import numpy as np
import cv2
image = cv2.imread('images\cat.jpg')
(x,y,z)=image.shape

cv2.imshow("image", image)
cv2.resizeWindow("image", y+100, x+100)
cv2.moveWindow('image', 100,100)


cv2.waitKey(0)
cv2.destroyAllWindows()