# We're going to want to bring in my led code from summerSensorSensation
# Eventually going to need the board and digitalIO imports to connect to LEDs and relays
# Probably an import needed to read bluetooth signals
import time
import driveCommands

drive = driveCommands.DriveTrain()

power = 1.0
while True:
    drive.tank(power)
    time.sleep(0.5)
    if power > -0.9:
        power -= 0.1
    else:
        power = 1
