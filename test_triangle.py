from triangle import triangle

def test_invalid1():
    assert triangle(-1, 0, 1) == -1

def test_normal():
    assert triagle(3, 4, 2) == 1

def test_isosceles():
    assert triangle(2, 2, 1) == 2

def test_equilateral():
    assert triangle(3, 3, 3) == 3

