import math
import pytest
from src import scientific_calc


def test_square_root_positive():
    assert scientific_calc.square_root(25) == 5.0
    assert scientific_calc.square_root(0) == 0.0
    assert scientific_calc.square_root(2) == math.sqrt(2)


def test_square_root_negative_raises():
    with pytest.raises(ValueError):
        scientific_calc.square_root(-4)


def test_square_root_invalid_type():
    with pytest.raises(TypeError):
        scientific_calc.square_root("nine")


def test_power():
    assert scientific_calc.power(2, 3) == 8.0
    assert scientific_calc.power(5, 0) == 1.0
    assert scientific_calc.power(9, 0.5) == 3.0
    assert scientific_calc.power(2, -1) == 0.5


def test_power_invalid_type():
    with pytest.raises(TypeError):
        scientific_calc.power("two", 3)


def test_logarithm_natural():
    assert scientific_calc.logarithm(math.e) == pytest.approx(1.0)
    assert scientific_calc.logarithm(1) == pytest.approx(0.0)


def test_logarithm_custom_base():
    assert scientific_calc.logarithm(100, 10) == pytest.approx(2.0)
    assert scientific_calc.logarithm(8, 2) == pytest.approx(3.0)


def test_logarithm_invalid_input():
    with pytest.raises(ValueError):
        scientific_calc.logarithm(0)
    with pytest.raises(ValueError):
        scientific_calc.logarithm(-5)
    with pytest.raises(ValueError):
        scientific_calc.logarithm(10, 1)


def test_sine():
    assert scientific_calc.sine(0) == pytest.approx(0.0)
    assert scientific_calc.sine(90) == pytest.approx(1.0)
    assert scientific_calc.sine(30) == pytest.approx(0.5)
    assert scientific_calc.sine(180) == pytest.approx(0.0)


def test_cosine():
    assert scientific_calc.cosine(0) == pytest.approx(1.0)
    assert scientific_calc.cosine(90) == pytest.approx(0.0, abs=1e-9)
    assert scientific_calc.cosine(60) == pytest.approx(0.5)
    assert scientific_calc.cosine(180) == pytest.approx(-1.0)


def test_tangent():
    assert scientific_calc.tangent(0) == pytest.approx(0.0)
    assert scientific_calc.tangent(45) == pytest.approx(1.0)


def test_tangent_undefined():
    with pytest.raises(ValueError):
        scientific_calc.tangent(90)


def test_factorial():
    assert scientific_calc.factorial(0) == 1
    assert scientific_calc.factorial(1) == 1
    assert scientific_calc.factorial(5) == 120
    assert scientific_calc.factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError):
        scientific_calc.factorial(-1)


def test_factorial_non_integer():
    with pytest.raises(TypeError):
        scientific_calc.factorial(3.5)
    
