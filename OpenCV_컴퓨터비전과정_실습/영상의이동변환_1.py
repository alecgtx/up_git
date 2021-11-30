import cv2
import numpy as np

src = cv2.imread('images/parasol.jpg')
if src is None:
    print('Image load failed!')
    sys.exit()
aff = np.array([[1, 0, -200],
                [0, 1, -100]], dtype=np.float32)
dst = cv2.warpAffine(src, aff, (0, 0))
cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()



