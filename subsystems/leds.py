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
        self.ani = 0
        self.mod = 10

    def message(self, colorA, colorB, message):
        """Runs the binary message in the colors specified"""
        if not self.begun:
            self.messageSetup(message)
            self.begun = True
        self.ani += 1
        if self.ani % self.mod == 0:
            self.ani = 0
            for i in range(self.qty):
                if self.digits[i] == 0:
                    self.leds[i] = colorA
                if self.digits[i] == 1:
                    self.leds[i] = colorB
            self.digits = self.digits[1:] + self.digits[:1]
            self.leds.show()

    def rotate(self, colorA, colorB, section):
        """Rotates between 2 colors, with the specified section length"""
        if not self.begun:
            self.rotateSetup(colorA, colorB, section)
            self.begun = True
        self.ani += 1
        if self.ani % self.mod == 0:
            self.ani = 0
            self.leds[self.qty - 1] = self.leds[0]
            for i in range(self.qty - 1):
                self.leds[i] = self.leds[i + 1]
                self.leds.show()

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

    def rainbow_cycle(self, wait):
        """Rainbow cycle code, runs a while true loop, so be careful"""
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
    def rotateSetup(self, colorA, colorB, section):
        for i in range(self.qty):
            if i % section == 0:
                self.primary = not self.primary
            if self.primary:
                self.leds[i - self.rotateCheck] = colorA
            else:
                self.leds[i - self.rotateCheck] = colorB
