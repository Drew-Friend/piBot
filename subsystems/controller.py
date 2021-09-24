# wm = None
# i=2
# while not wm:
#   try:
#     wm=cwiid.Wiimote()
#   except RuntimeError:
#     if (i>10):
#       quit()
#       break
#     print "Error opening wiimote connection"
#     print "attempt " + str(i)
#     i +=1


class wiiMote:
    def __init__(self):
        import cwiid

        self.wii = cwiid.Wiimote()
        self.wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.buttons = self.wii.state["buttons"]
        self.accel = self.wii.state["acc"]
        # consistent Buttons
        self.x = False
        self.y = False
        self.a = False
        self.b = False
        self.turn = 0
        self.throttle = 0

        # wii specific
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.minus = False
        self.plus = False
        self.home = False
        self.wii.led = 1
        self.vibing = False

    def readOutput(self):
        self.accel = self.wii.state["acc"]
        self.buttons = self.wii.state["buttons"]
        if self.buttons:
            if self.wii.BTN_LEFT:
                self.left = True
            if self.wii.BTN_RIGHT:
                self.right = True
            if self.wii.BTN_UP:
                self.up = True
            if self.wii.BTN_DOWN:
                self.down = True
            if self.wii.BTN_1:
                self.x = True
            if self.wii.BTN_2:
                self.y = True
            if self.wii.BTN_A:
                self.a = True
            if self.wii.BTN_B:
                self.b = True
            if self.wii.BTN_MINUS:
                self.minus = True
            if self.wii.BTN_PLUS:
                self.plus = True
            if self.wii.BTN_HOME:
                self.home = True

    def cycle_leds(self):
        if self.wii.led == 1:
            self.wii.led = 0
        elif self.wii.led == 0:
            self.wii.led = 3
        elif self.wii.led == 3:
            self.wii.led = 8
        else:
            self.wii.led = 1

    def vibrate_toggle(self):
        self.vibing = not self.vibing
        self.wii.rumble = self.vibing


class debugTerminal:
    def __init__(self):
        import serial

        self.serialPort = serial.Serial("/dev/rfcomm1", baudrate=9600)
        serial.flushOutput()
        serial.flushInput()

        self.two = False
        self.x = False
        self.y = False
        self.a = False
        self.b = False
        self.turn = 0
        self.throttle = 0

    def readOutput(self):
        self.serialPort.flushOutput()
        out = self.serialPort.readline().decode()
        print(out)
        # print(serial.readline().decode())
        if out == "b":
            self.b = not self.b
            self.serialPort.flushInput()
        if out == "a":
            self.a = not self.a
            self.serialPort.flushInput()
        elif out != "":
            self.throttle = float(out)
            self.serialPort.flushInput()


class emptyTester:
    def __init__(self):
        self.two = False
        self.x = False
        self.y = False
        self.a = False
        self.b = False
        self.turn = 0
        self.throttle = 0

    def readOutput(self):
        pass
