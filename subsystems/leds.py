import board
import neopixel
import time
import sys


class Strand:
    """Valid pins:  board.D10, board.D12, board.D18, and board.D21"""

    def __init__(self, pin, num):
        self.cycle = 0
        self.rotateCheck = 0
        self.qty = num
        self.offset = 0
        self.digits = []
        self.firstRun = True
        self.primary = True
        self.leds = neopixel.NeoPixel(pin, self.qty)
        self.bounceI = 0
        self.forward = True
        self.begun = False

    # Runs the binary message in the colors specified
    def message(self, colorA, colorB, message):
        if not self.begun:
            self.messageSetup(message)
            self.begun = True
        for i in range(self.qty):
            if self.digits[i] == 0:
                self.leds[i] = colorA
            if self.digits[i] == 1:
                self.leds[i] = colorB
        digits = self.digits[1:] + self.digits[:1]
        self.leds.show()

    # Rotates between 2 colors
    def rotate(self, colorA, colorB, length, section):
        if not self.begun:
            self.rotateSetup(colorA, colorB, length, section)
            self.begun = True
        self.leds[self.qty - 1] = self.leds[0]
        for i in range(self.qty - 1):
            self.leds[i] = self.leds[i + 1]
            self.leds.show()

    # Think Wiimote trying to connect. LED bounces between the endpoints
    def bounce(self):
        bounceColor = (0, 100, 255)
        self.leds[self.bounceI] = (0, 0, 0)
        if self.bounceI == self.qty or self.bounceI == 0:
            self.forward = not self.forward
        if self.forward:
            self.bounceI += 1
        else:
            self.bounceI -= 1
        self.leds[self.bounceI] = bounceColor

    # GAY!! fun pretty estop code
    def rainbow_cycle(self, wait):
        while True:
            for j in range(255):
                for i in range(self.qty):
                    pixel_index = (i * 256 // self.qty) + j
                    self.leds[i] = self.wheel(pixel_index & 255)
                self.leds.show()
                time.sleep(wait)

    # Helper Functions:

    # Wheel is used by the rainbow to...rainbow
    def wheel(self, pos):
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)

    # sets up the message to run in binary
    def messageSetup(self, message):
        res = "".join(format(ord(i), "b") for i in message)
        for i in res:
            self.digits.append(i)

    # Sets all initial endpoints, small issue if length has a remainder of sections
    def rotateSetup(self, colorA, colorB, length, section):
        for i in range(length):
            if i % section == 0:
                self.primary = not self.primary
            if self.primary:
                self.leds[i - self.rotateCheck] = colorA
            else:
                self.leds[i - self.rotateCheck] = colorB
