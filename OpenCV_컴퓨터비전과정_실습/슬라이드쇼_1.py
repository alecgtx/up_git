import sys
import cv2
import glob

img_files = glob.glob('cars\*.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])
    if img is None:
        print('Image load failed!')
        break
    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:
        break
    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()

cv2.imshow('image', )
while True :
    key = cv2.waitKey()
    if key == 27 : # ESC키
        break
    elif key == ord('s') or key == ord('S'):
        img = ~img # ~ : NOT
        cv2.imshow('image', img)
cv2.destroyAllWindows()