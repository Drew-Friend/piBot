import board
from digitalio import DigitalInOut

# 6, 13, 19, 26
class Relay:
    """Valid ports are board.D6, board.D13, board.D19, board.D26"""

    def __init__(self, port):
        self.port = DigitalInOut(port)
        self.port.switch_to_output(value=False)

    def on(self):
        self.port.value = True

    def off(self):
        self.port.value = False

    def toggle(self):
        self.port.value = not self.port.value


class Pair:
    """Valid ports are board.D6, board.D13, board.D19, board.D26"""

    def __init__(self, port1, port2):
        self.motor1 = Relay(port1)
        self.motor2 = Relay(port2)

    def on(self):
        self.motor1.on()
        self.motor2.on()

    def off(self):
        self.motor1.off()
        self.motor2.off()

    def toggle(self):
        if self.motor1.port.value:
            self.off()
        else:
            self.on()
