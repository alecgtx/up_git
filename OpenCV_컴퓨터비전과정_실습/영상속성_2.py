import cv2
image1 = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('images\cat.bmp', cv2.IMREAD_COLOR)

h, w = image1.shape[:2]

for y in range(h):
    for x in range(w):
        image1[y, x] = 255 #흰색
        image2[y, x] = (0, 0, 255) #(B,G,R)빨간색

image1[:,:] = 255
image2[:,:] = (0, 0, 255)

cv2.namedWindow('image1')
cv2.namedWindow('image2')
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
