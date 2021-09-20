# We're going to want to bring in my led code from summerSensorSensation
# Eventually going to need the board and digitalIO imports to connect to LEDs and relays
# Probably an import needed to read bluetooth signals
import time
from driveCommands import DriveTrain as drive

while True:
    drive.tank(0)
    time.sleep(1)
    drive.tank(1)
    time.sleep(1)
    drive.tank(0)
    time.sleep(1)
    drive.tank(-1)
