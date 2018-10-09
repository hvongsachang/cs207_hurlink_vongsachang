import pytest
import L2

def test_quadroots_result():
    assert L2.L2([1.0, 1.0, 1.0], [3.0, 4.0, 5.0]) == 7.0710678118654755
    assert L2.L2([3.0, 4.0, 5.0]) == 7.0710678118654755
    
def test_quadroots_types():
    with pytest.raises(TypeError):
        L2.L2(['3', '4', '5'])

def test_quadroots_zerocoeff():
    with pytest.raises(ValueError):
        L2.L2([1.0, 1.0, 1.0], [3.0, 4.0, 5.0, 9999.0])