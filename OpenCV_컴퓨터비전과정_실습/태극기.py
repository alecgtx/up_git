import cv2
import sys
import numpy as np

img=np.full((400,600,3), 255, np.uint8)

cv2.circle(img, (300, 200), 50, (0, 0, 255), -1, cv2.LINE_AA)
cv2.rectangle(img, (240, 200), (360, 260), (255, 255, 255), -1)
cv2.circle(img, (325, 200), 25, (255, 0, 0), -1, cv2.LINE_AA)
cv2.ellipse(img, (300,200), (50,50), 0, 0, 180, 255, -1)
cv2.circle(img, (275, 200), 25, (0, 0, 255), -1, cv2.LINE_AA)

text = "Korean Flag"
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_DUPLEX, 0.8,
(0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
