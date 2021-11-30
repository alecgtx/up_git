import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
tilt=125
pan=0
kit.servo[0].angle = pan
kit.servo[1].angle = tilt
#kit.continuous_servo[1].throttle = 1
#time.sleep(1)
#kit.continuous_servo[1].throttle = -1
#time.sleep(1)
#kit.servo[0].angle = 0
#kit.continuous_servo[1].throttle = 0
for i in range(0,180):
    kit.servo[0].angle=i
    time.sleep(0.05)
for i in range(180,0,-1):
    kit.servo[0].angle=i
    time.sleep(0.05)
for i in range(45,170):
    kit.servo[1].angle=i
    time.sleep(0.05)
for i in range(170,45,-1):
    kit.servo[1].angle=i
    time.sleep(0.05)