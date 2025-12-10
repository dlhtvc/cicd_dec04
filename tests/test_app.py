import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (
    add,
    subtract,
    multiply,
    divide,
    log,
    square,
    sin,
    cos,
    square_root,
    percentage
)


def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 7) == 21

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) is None

def test_log_valid():
    # log base 2 of 8 is 3
    assert log(8, 2) == 3

def test_log_invalid_x():
    assert log(0, 10) is None
    assert log(-5, 10) is None

def test_log_invalid_base():
    assert log(10, 0) is None
    assert log(10, 1) is None
    assert log(10, -2) is None

def test_square():
    assert square(5) == 25

def test_sin_radians():
    assert sin(0) == 0

def test_sin_degrees():
    assert math.isclose(sin(90, degrees=True), 1.0, rel_tol=1e-9)

def test_cos_radians():
    assert cos(0) == 1

def test_cos_degrees():
    assert math.isclose(cos(60, degrees=True), 0.5, rel_tol=1e-9)

def test_square_root_positive():
    assert square_root(16) == 4

def test_square_root_negative():
    assert square_root(-1) is None

def test_percentage_normal():
    assert percentage(20, 50) == 40.0

def test_percentage_div_by_zero():
    assert percentage(10, 0) is None