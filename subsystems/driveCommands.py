class analogDrive:
    def __init__(self, add=0x40):
        from adafruit_motorkit import MotorKit

        self.kit = MotorKit(add)
        self.m1 = self.kit.motor1
        self.m2 = self.kit.motor2
        self.booster = 0.5

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


class digitalDrive:
    def __init__(self, l1, l2, r1, r2):
        import board
        import relays

        self.left = relays.Reversible(l1, l2)
        self.right = relays.Reversible(r1, r2)

    def indiv(self, p1, p2):
        if p1 < 0:
            self.left.reverse()
        elif p1 == 0:
            self.left.off()
        else:
            self.left.forward()

        if p2 < 0:
            self.right.reverse()
        elif p2 == 0:
            self.right.off()
        else:
            self.right.forward()

    def tank(self, power):
        self.indiv(power, power)

    def arcade(self, driveVal, turnVal):
        """1 for forward and right, 0 for none, -1 for backward and left"""
        pL = driveVal - turnVal
        pR = driveVal + turnVal
        self.indiv(pL, pR)

    def off(self):
        self.indiv(0, 0)
