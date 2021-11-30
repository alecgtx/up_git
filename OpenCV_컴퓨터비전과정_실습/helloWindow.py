import sys
import cv2

image = cv2.imread('images\cat.bmp', cv2.IMREAD_UNCHANGED)
print(image.shape)
print(image)

image2 = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
print(image2.shape)
print(image2)

if image is None:
    print('Image Load failed!')
    sys.exit()


cv2.namedWindow('image')
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()