import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('images\cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)


plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
