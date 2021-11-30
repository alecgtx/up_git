def findFace(img):
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

myFacesListC = []
myFaceListArea = []

for (x, y, w, h) in faces:
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cx = x + w//2
cy = y + h//2
area = w*h
myFacesListC.append([cx,cy])
myFaceListArea.append(area)

if len(myFaceListArea) != 0:
i = myFaceListArea.index(max(myFaceListArea))
# index of closest face
return img,[myFacesListC[i],myFaceListArea[i]]
else:
return img, [[0,0],0]

## STEP 2
img, c = findFace(img)