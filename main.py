# Python imports and my classes
import time
import board
from subsystems import driveCommands, ble, controller, leds, relays

# Instantiate the subsystems used on the robot
drive = driveCommands.analogDrive(0x40)
bt = ble.btComm("00:00:00:00:00:00")
controls = controller.emptyTester(bt.sock)
backLight = leds.Strand(board.D21, 15)
spinner = relays.Pair(board.D6, board.D13)
spinnerPrev = False
boostPrev = False
connected = False


def periodic():
    global spinnerPrev
    global boostPrev
    try:
        controls.readOutput()
    except:
        bt.sock = None
        return None

    if controls.b and not boostPrev:
        drive.toggle_SUPER_ULTRA_MEGA_GOD_MODE()
        boostPrev = True
    if boostPrev and not controls.b:
        boostPrev = False

    if controls.a and not spinnerPrev:
        spinner.toggle()
        spinnerPrev = True
    if spinnerPrev and not controls.a:
        spinnerPrev = False

    drive.arcade(controls.throttle, controls.turn)
    print(
        "Motor 1: {}, Motor 2: {}, Spinner: {}".f(
            drive.m1, drive.m2, spinner.motor2.port.value
        )
    )


# Loop after everything has been initialized
while True:
    drive.off()
    spinner.off()
    while not bt.sock.isConnected():
        backLight.bounce()
        bt.scan()

    backLight.rotate()
    periodic()
