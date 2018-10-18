import pytest
import Complex

class TestComplex:

    def test_magnitude(self):
        assert Complex.Complex(3,4).magnitude() == 5.0

    def test_angle(self):
        assert Complex.Complex(3,4).angle() == 53.13010235415598

    def test_polar(self):
        assert Complex.Complex(3,4).polar() == (5.0, 53.13010235415598)

    def test_conjugate(self):
        assert Complex.Complex(3,4).conjugate() == Complex.Complex(3,-4)
    
    def test_types(self):
        with pytest.raises(ValueError):
            Complex.Complex(3,4) + "Complex number"