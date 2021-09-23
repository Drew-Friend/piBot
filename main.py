# Python imports and my classes
import time
import board
from subsystems import driveCommands, controller, leds, relays

# Instantiate the subsystems used on the robot
drive = driveCommands.DriveTrain()
# controls = controller.wiiMote()
controls = controller.debugTerminal()
backLight = leds.Strand(board.D21, 15)
spinner = relays.Pair(board.D6, board.D13)
spinnerPrev = False
boostPrev = False


def periodic():
    global spinnerPrev
    global boostPrev
    controls.readOutput()
    drive.arcade(controls.throttle, controls.turn)

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

    print(
        "Motor 1: {}, Motor 2: {}, Spinner: {}".f(
            drive.m1, drive.m2, spinner.motor2.port.value
        )
    )


connected = False
# Loop after everything has been initialized
while True:
    drive.off()
    spinner.off()
    while not connected:
        backLight.bounce()
        # For loop makes it so LEDs don't update on every loop, so the animation is slower
        for i in range(10):
            # Bluetooth search function
            pass

    while connected:
        backLight.rotate()
        # For loop makes it so LEDs don't update on every loop, so the animation is slower
        for i in range(10):
            periodic()
