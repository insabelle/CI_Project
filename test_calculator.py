from calculator import *

def test_addition():
    assert addition(4, 2) == 6

def test_soustraction():
    assert soustraction(5, 2) == 3

def test_multiplication():
    assert multiplication(3, 2) == 6

def test_division():
    assert division(8, 2) == 4

def test_division_par_zero():
with pytest.raises(ValueError):
division(8, 0)


def test_puissance():
    assert puissance(2, 3) == 8
    assert puissance(5, 0) == 1