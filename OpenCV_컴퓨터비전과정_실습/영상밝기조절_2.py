
import cv2

src1 = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
src2 = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

alpha, beta=0.3, 0.5

dst1=cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2=cv2.add(src1*alpha, src2*beta)


titles=['src1','src2','dst1','dst2']
for t in titles:
    cv2.imshow(t, eval(t))


#cv2.imshow('src1', src1)
#cv2.imshow('src2', src2)
#cv2.imshow('dst1', dst1)
#cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()