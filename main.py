# We're going to want to bring in my led code from summerSensorSensation
# Eventually going to need the board and digitalIO imports to connect to LEDs and relays
# Probably an import needed to read bluetooth signals
from adafruit_motorkit import MotorKit
import time


# Set up motors on i2c address 40
kit = MotorKit(0x40)
# I think they default to 0, but this is the easiest way to make sure I remember the command
kit.motor1.throttle = 0
kit.motor2.throttle = 0

while True:
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    time.sleep(1)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    time.sleep(1)
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1
    time.sleep(1)
