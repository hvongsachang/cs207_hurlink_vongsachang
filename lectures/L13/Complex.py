"""This module creates object representations of complex numbers."""
import math
class Complex(object):
    """This class creates a complex number and has basic operations of a complex number.
    
    INPUT
    ===========
    a = the real number, of type int
    b = the imaginary part, of type int

    EXAMPLES
    ===========
    >>> cnum = Complex(3,4)
    >>> cnum.magnitude()
    5.0
    >>> cnum.angle()
    53.13010235415598
    >>> cnum.polar()
    (5.0, 53.13010235415598)
    >>> connum = cnum.conjugate()
    >>> connum.a
    3
    >>> connum.b
    -4
    >>> added = cnum + connum
    >>> added.polar()
    (6, 0)
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def magnitude(self):
        return math.sqrt((self.a ** 2 + self.b ** 2))

    def angle(self):
        return math.degrees(math.atan(self.b / self.a))

    def polar(self):
        return (self.magnitude(), self.angle())

    def conjugate(self):
        return Complex(self.a, -self.b)

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __radd__(self, other):
        if type(other) == int:
            return Complex(self.a + other, self.b)
        else:
            raise ValueError
