import math
class RealExtensions(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class _Complex(RealExtensions):
    def _magnitude(self):
        return math.sqrt((self.a ** 2 + self.b ** 2))
    def _angle(self):
        return math.degrees(math.atan(self.b / self.a))
    def polar(self):
        return (self._magnitude(), self._angle())

class Dual(RealExtensions):
    def _magnitude(self):
        return self.a
    def _angle(self):
        return self.b/self.a
    def polar(self):
        return (self._magnitude(), self._angle())
