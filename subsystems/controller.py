import cwiid

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
        self.wii = cwiid.Wiimote()
        self.wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.buttons = self.wii.state["buttons"]
        self.accel = self.wii.state["acc"]
        self.one = False
        self.two = False
        self.a = False
        self.b = False
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.right = False
        self.minus = False
        self.plus = False
        self.home = False
        self.wii.led = 1
        self.vibing = False
        self.turn
        self.throttle

    def readOutput(self):
        self.accel = self.wii.state["acc"]
        self.buttons = self.wii.state["buttons"]
        if self.buttons:
            if cwiid.BTN_LEFT:
                self.left = True
            if cwiid.BTN_RIGHT:
                self.right = True
            if cwiid.BTN_UP:
                self.up = True
            if cwiid.BTN_DOWN:
                self.down = True
            if cwiid.BTN_1:
                self.one = True
            if cwiid.BTN_2:
                self.two = True
            if cwiid.BTN_A:
                self.a = True
            if cwiid.BTN_B:
                self.b = True
            if cwiid.BTN_MINUS:
                self.minus = True
            if cwiid.BTN_PLUS:
                self.plus = True
            if cwiid.BTN_HOME:
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
