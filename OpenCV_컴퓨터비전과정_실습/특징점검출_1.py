
import cv2
import sys
import numpy as np
import math

src1 = cv2.imread('images/hough2.jpg', cv2.IMREAD_GRAYSCALE)
#src2 = cv2.imread('images/hough_resize.jpg', cv2.IMREAD_GRAYSCALE)

#feature = cv2.KAZE_create()
feature = cv2.AKAZE_create()
#feature = cv2.ORB_create()
#feature = cv2.xfeatures2d.SIFT_create()

kp1 = feature.detect(src1)
#kp2 = feature.detect(src2)


dst1 = cv2.drawKeypoints(src1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#dst2 = cv2.drawKeypoints(src2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print('# of kp1:', len(kp1))
#print('# of kp2:', len(kp2))


cv2.imshow('dst1', dst1)
#cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()


