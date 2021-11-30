import cv2
import numpy as np

src = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = np.zeros_like(src)
cv2.circle(mask, (350,200), 130, (255,255,255), -1)
masked=cv2.bitwise_and(src, mask)



cv2.imshow("masked", masked)


cv2.waitKey(0)
cv2.destroyAllWindows()
