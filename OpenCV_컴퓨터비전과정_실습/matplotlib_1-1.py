import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('images\cat.bmp')
# imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

b, g, r=cv2.split(imgBGR)
imgBGR=cv2.merge([r,g,b])

plt.axis('off')
plt.imshow(imgBGR)
plt.show()

imgGray = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()
