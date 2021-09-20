from adafruit_motorkit import MotorKit


class DriveTrain:
    def __innit__(self):
        self.kit = MotorKit(0x40)

    def arcade(self, x, y):
        pass

    def tank(self, p1, p2):
        self.kit.motor1.throttle = p1
        self.kit.motor2.throttle = p2

    def tank(self, power):
        self.kit.motor1.throttle = power
        self.kit.motor2.throttle = power
