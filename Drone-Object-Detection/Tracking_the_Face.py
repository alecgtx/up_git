# PID Controller

def trackFace(myDrone,c,w,pid,pError):
print(c)
## PIDerror = c[0][0] - w//2   
# Current Value - Target Value
speed = int(pid[0]*error + pid[1] * (error-pError))

# Sending Rotation to Drone

if c[0][0] != 0:
myDrone.yaw_velocity = speed
else:
myDrone.left_right_velocity = 0
myDrone.for_back_velocity = 0
myDrone.up_down_velocity = 0
myDrone.yaw_velocity = 0
error = 0
# SEND VELOCITY VALUES TO TELLO
if myDrone.send_rc_control:
myDrone.send_rc_control(myDrone.left_right_velocity,myDrone.for_back_velocity,
myDrone.up_down_velocity, myDrone.yaw_velocity)

	## STEP 3
pError = trackFace(myDrone,c,w,pid,pError)