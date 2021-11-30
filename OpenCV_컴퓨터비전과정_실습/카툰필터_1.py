import cv2
#import numpy as np

def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))
    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    return dst
def pencil_sketch_filter(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(gray, blr, scale=255)
    return dst
def original(img):
    return img

filter_list = [cartoon_filter, pencil_sketch_filter, original]

cap = cv2.VideoCapture(0)
counter = 0
while True: # 카메라 프레임 처리
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # 좌우 반전
#    dst = cv2.Canny(frame, 120, 180)
    if ret:
        dst=filter_list[counter](frame)
        cv2.imshow('dst', dst)
        key = cv2.waitKey(10)
        if key==27:
            break
        elif key == ord(" "):
            counter +=1
            if counter>len(filter_list)-1:
                counter = 0

cap.release()
cv2.destroyAllWindows()






