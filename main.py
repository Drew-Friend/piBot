# Python imports and my classes
import time
import board
from subsystems import driveCommands, controller, leds, relays

# Instantiate the subsystems used on the robot
drive = driveCommands.DriveTrain()
remote = controller.wiiMote()
backLight = leds.Strand(board.D21, 15)
spinner = relays.Pair(board.D6, board.D13)

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

    spinner.toggle()
    drive.tank(power)
    backLight.bounce()
    time.sleep(1)

drive.tank(0)
