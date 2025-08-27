import pytest
from homework_15 import Romb

def test_valid_only_angle_a():
    r = Romb(5, angle_a=60)
    assert r.angle_a == 60
    assert r.angle_b == 120

def test_valid_only_angle_b():
    r = Romb(5, angle_b=60)
    assert r.angle_a == 120
    assert r.angle_b == 60

def test_valid_with_two_angles():
    r = Romb(5, angle_a=70, angle_b=110)
    assert r.angle_a + r.angle_b == 180

def test_missing_both_angles():
    with pytest.raises(ValueError, match="At least one angle must be provided"):
        Romb(5)

def test_invalid_side():
    with pytest.raises(ValueError, match="must be greater than 0"):
        Romb(-3, angle_a=60)

def test_invalid_angle_value():
    with pytest.raises(ValueError, match="must be between 0 and 180"):
        Romb(5, angle_a=190)

def test_invalid_angle_sum():
    with pytest.raises(ValueError, match="Sum of angles must be 180"):
        Romb(5, angle_a=100, angle_b=100)