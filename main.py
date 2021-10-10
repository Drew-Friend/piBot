# Python imports and my classes
import time
import board
from subsystems import driveCommands, ble, controller, leds, relays

# Instantiate the subsystems used on the robot
drive = driveCommands.analogDrive(0x40)
bt = ble.btComm("C8:D7:B0:AF:F3:4F")
controls = controller.emptyTester(bt.sock)
backLight = leds.Strand(board.D21, 15)
spinner = relays.Pair(board.D6, board.D13)
spinnerPrev = False
boostPrev = False
connected = False


def periodic():
    global spinnerPrev
    global boostPrev
    if bt.isConnected():
        controls.readOutput()

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
        backLight.animate((100, 0, 255), (0, 0, 255), "rotate")
        print(
            "Motor 1: {}, Motor 2: {}, Spinner: {}".f(
                drive.m1, drive.m2, spinner.motor2.port.value
            )
        )


def test():
    testR1 = relays.Standard(board.D19)
    testR1.on()
    testR2 = relays.Standard(board.D26)
    iter = 0
    power = 0.75
    while True:
        if iter % 5 == 0:
            iter = 0
            spinner.toggle()
        testR1.toggle()
        testR2.toggle()
        backLight.animate((100, 0, 255), (0, 0, 255), "rotate")
        power = -1 * power
        drive.tank(power)
        time.sleep(0.5)


# Loop after everything has been initialized
while True:
    drive.off()
    spinner.off()
    # Comment out the test line if actually running the robot
    test()
    while not bt.isConnected():
        backLight.bounce()
        print("scanning...")
        bt.scan()

    periodic()
