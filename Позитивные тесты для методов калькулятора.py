import math
# test_addition - объявление функции сложения
def test_addition():
    result = math.add(2, 3)
    assert result == 5

def test_subtraction():
    result = math.subtract(5, 2)
    assert result == 3

def test_multiplication():
    result = math.multiply(4, 6)
    assert result == 24

def test_division():
    result = math.divide(10, 2)
    assert result == 5

def test_power():
    result = math.power(2, 4)
    assert result == 16
