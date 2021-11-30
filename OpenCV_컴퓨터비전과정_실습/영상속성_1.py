import cv2
image = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
#img2 = cv2.imread('images\cat.bmp', cv2.IMREAD_COLOR)
print(type(image))
print(image.ndim)
print(image.shape)
print(image.size)
print(image.dtype)
