from adafruit_motorkit import MotorKit


class DriveTrain:
    def __init__(self):
        self.kit = MotorKit(0x40)
        self.m1 = self.kit.motor1
        self.m2 = self.kit.motor2
        self.booster = 0.5
        print("innited")

    def indiv(self, p1, p2):
        self.m1.throttle = p1 * self.booster
        self.m2.throttle = p2 * self.booster

    def tank(self, power):
        self.indiv(power, power)

    def arcade(self, power, turnval):
        p1 = power + 0.5 * turnval
        p2 = power - 0.5 * turnval
        if p1 > 1:
            p1 = 1
        elif p1 < -1:
            p1 = -1
        if p2 > 1:
            p2 = 1
        elif p2 < -1:
            p2 = -1
        self.indiv(p1, p2)

    def off(self):
        self.indiv(0, 0)

    def toggle_SUPER_ULTRA_MEGA_GOD_MODE(self):
        if self.booster < 1:
            self.booster = 1
        else:
            self.booster = 0.5
