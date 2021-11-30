

import numpy as np
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('images/lenna.bmp')
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)
for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
cv2.imshow('src', src)
cv2.waitKey(1)
plt.show()


cv2.destroyAllWindows()

