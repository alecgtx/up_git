
import cv2

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
dst1=cv2.add(src, 100)
dst2=cv2.add(src, -100)




cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()