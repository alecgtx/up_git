from djitellopy
import Telloimport cv2

def intializeTello():
# CONNECT TO TELLO
myDrone = Tello()
myDrone.connect()
myDrone.for_back_velocity = 0
myDrone.left_right_velocity = 0
myDrone.up_down_velocity = 0
myDrone.yaw_velocity = 0
myDrone.speed =0
print(myDrone.get_battery())
myDrone.streamoff()
myDrone.streamon()
return myDrone

myDrone = intializeTello()


# Get Frame from Drone

def telloGetFrame(myDrone,w=360,h=240):
# GET THE IMGAE FROM TELLO
myFrame = myDrone.get_frame_read()
myFrame = myFrame.frame
img = cv2.resize(myFrame, (w, h))
return img

while True:
## STEP 1
img = telloGetFrame(myDrone)
# DISPLAY IMAGE
cv2.imshow("MyResult", img)
# WAIT FOR THE 'Q' BUTTON TO STOP
if cv2.waitKey(1) and 0xFF == ord('q'):
# replace the 'and' with '&amp;' 
myDrone.land()
break