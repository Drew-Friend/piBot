from adafruit_motorkit import MotorKit


class DriveTrain:
    def __innit__(self):
        self.kit = MotorKit(0x40)
        self.m1 = self.kit.motor1
        self.m2 = self.kit.motor2

    def arcade(self, x, y):
        pass

    def tank(self, p1, p2):
        self.m1.throttle = p1
        self.m2.throttle = p2

    def tank(self, power):
        self.m1.throttle = power
        self.m2.throttle = power
