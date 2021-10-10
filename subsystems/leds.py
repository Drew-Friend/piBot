import board
import neopixel


class Strand:
    """Valid pins:  board.D10, board.D12, board.D18, and board.D21"""

    def __init__(self, pin, num):
        # Bounce
        self.bounceI = 0
        self.forward = True
        # General
        self.section = 4
        self.qty = self.section - (num % self.section) + num
        self.leds = neopixel.NeoPixel(pin, self.qty)
        self.begun = False
        self.ani = 0
        self.mod = 10
        self.valList = []

    def bounce(self):
        """Think Wiimote trying to connect. LED bounces between the endpoints"""
        # Because this code disrupts the normal pattern, I want to reinit when it switches back
        self.begun = False
        bounceColor = (0, 100, 255)
        self.leds[self.bounceI] = (0, 0, 0)
        if self.forward:
            self.bounceI += 1
        else:
            self.bounceI -= 1
        if self.bounceI == self.qty - 1 or self.bounceI == 0:
            self.forward = not self.forward
        self.leds[self.bounceI] = bounceColor
        self.leds.show()

    def animate(self, A=(0, 0, 0), B=(0, 0, 0), type="", message=""):
        """Valid types are "rotate" and "message", defaults to rainbow code if not given anything else."""
        if not self.begun:
            if type == "rotate":
                self.rotateSetup(A, B)
            elif type == "message":
                self.messageSetup(A, B, message)
            else:
                self.rainbowSetup()
            self.begun = True
        if self.ani % self.mod == 0:
            self.ani = 0
            for i in range(self.qty):
                self.leds[i] = self.valList[i]
            self.valList = self.valList[1:] + self.valList[:1]
            self.leds.show()

        self.ani += 1

    # Setup Functions:
    # Sets up the message as hex codes for the 2 colors chosen
    def messageSetup(self, colorA, colorB, message):
        self.valList.clear
        res = "".join(format(ord(i), "b") for i in message)
        while len(self.valList) < self.qty:
            for i in res:
                if i == "1":
                    self.valList.append(colorA)
                else:
                    self.valList.append(colorB)

    # List of hex codes, alternating with a section length of 4
    def rotateSetup(self, colorA, colorB):
        self.valList.clear
        primary = True
        # Make sure the string has all equal sections
        for i in range(self.qty):
            if i % self.section == 0:
                primary = not primary
            if primary:
                self.valList.append(colorA)
            else:
                self.valList.append(colorB)

    # Creates a list twice as long as the LED string with smooth tranistions
    def rainbowSetup(self):
        self.valList.clear
        mult = 255 // (self.qty / 3)
        # G++(>Yellow)
        for i in range(self.qty // 3):
            self.valList.append((255, int(i * mult), 0))
        # R--(>Green)
        for i in range(self.qty // 3):
            self.valList.append((255 - int(i * mult), 255, 0))
        # B++(>Cyan)
        for i in range(self.qty // 3):
            self.valList.append((0, 255, int(i * mult)))
        # G--(>Blue)
        for i in range(self.qty // 3):
            self.valList.append((0, 255 - int(i * mult), 255))
        # R++(>Purple)
        for i in range(self.qty // 3):
            self.valList.append((int(i * mult), 0, 255))
        # B--(>Red)
        for i in range(self.qty // 3):
            self.valList.append((255, 0, 255 - int(i * mult)))
