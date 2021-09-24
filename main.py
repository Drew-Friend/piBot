# Python imports and my classes
import time
import board
from subsystems import driveCommands, controller, relays

# Instantiate the subsystems used on the robot
drive = driveCommands.digitalDrive()
controls = controller.emptyTester()
spinner = relays.Pair(board.D6, board.D13)
spinnerPrev = False


def periodic():
    global spinnerPrev
    global boostPrev
    try:
        controls.readOutput()
    except:
        return False
    drive.arcade(controls.throttle, controls.turn)

    if controls.a and not spinnerPrev:
        spinner.toggle()
        spinnerPrev = True
    if spinnerPrev and not controls.a:
        spinnerPrev = False

    print(
        "Motor 1: {}, Motor 2: {}, Spinner: {}".f(
            drive.left, drive.right, spinner.motor2.port.value
        )
    )
    return True


connected = False
# Loop after everything has been initialized
while True:
    drive.off()
    spinner.off()
    while not connected:
        # Bluetooth search function
        pass

    while connected:
        connected = periodic()
