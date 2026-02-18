import math


def square_root(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number.")
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)


def power(base, exponent):
    if not (isinstance(base, (int, float)) and isinstance(exponent, (int, float))):
        raise TypeError("Both inputs must be numbers.")
    return math.pow(base, exponent)


def logarithm(x, base=math.e):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number.")
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number.")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    return math.log(x) / math.log(base)


def sine(angle_degrees):
    if not isinstance(angle_degrees, (int, float)):
        raise TypeError("Angle must be a number.")
    radians = math.radians(angle_degrees)
    return round(math.sin(radians), 10)


def cosine(angle_degrees):
    if not isinstance(angle_degrees, (int, float)):
        raise TypeError("Angle must be a number.")
    radians = math.radians(angle_degrees)
    return round(math.cos(radians), 10)


def tangent(angle_degrees):
    if not isinstance(angle_degrees, (int, float)):
        raise TypeError("Angle must be a number.")
    if angle_degrees % 180 == 90:
        raise ValueError("Tangent is undefined at 90, 270, ... degrees.")
    radians = math.radians(angle_degrees)
    return round(math.tan(radians), 10)


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    return math.factorial(n)

