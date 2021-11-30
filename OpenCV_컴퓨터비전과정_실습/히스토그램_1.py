

import numpy as np
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
cv2.imshow('src', src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()




cv2.destroyAllWindows()