from adafruit_motorkit import MotorKit


class DriveTrain:
    def __init__(self):
        self.kit = MotorKit(0x40)
        self.m1 = self.kit.motor1
        self.m2 = self.kit.motor2
        print("innited")

    def indiv(self, p1, p2):
        self.m1.throttle = p1
        self.m2.throttle = p2

    def tank(self, power):
        self.indiv(power, power)

    def arcade(self, power, turnval):
        p1 = power + turnval
        p2 = power - turnval
        if p1 > 1:
            p1 = 1
        elif p1 < -1:
            p1 = -1
        if p2 > 1:
            p2 = 1
        elif p2 < -1:
            p2 = -1
        self.indiv(p1, p2)
