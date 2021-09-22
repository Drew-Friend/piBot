# We're going to want to bring in my led code from summerSensorSensation
# Eventually going to need the board and digitalIO imports to connect to LEDs and relays
import time
import driveCommands
import controller

remote = controller.wiiMote()
drive = driveCommands.DriveTrain()

power = 1.0
# Connected will be used to shut off the robot if it loses connection, instead of running on the last command received
connected = True
while connected:
    if power < 0 and power > -0.15:
        power = 1
    elif power > 0 and power < 0.15:
        power = -1
    else:
        power = power * 0.5
    drive.tank(power)
    print(power)
    time.sleep(1)

drive.tank(0)
