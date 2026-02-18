import sys
import os
import math
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import scientific_calc


class TestSquareRoot(unittest.TestCase):

    def test_perfect_square(self):
        self.assertEqual(scientific_calc.square_root(16), 4.0)

    def test_zero(self):
        self.assertEqual(scientific_calc.square_root(0), 0.0)

    def test_irrational(self):
        self.assertAlmostEqual(scientific_calc.square_root(2), math.sqrt(2))

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            scientific_calc.square_root(-9)

    def test_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            scientific_calc.square_root("hello")


class TestPower(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(scientific_calc.power(2, 10), 1024.0)

    def test_zero_exponent(self):
        self.assertEqual(scientific_calc.power(99, 0), 1.0)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(scientific_calc.power(27, 1/3), 3.0, places=5)

    def test_negative_exponent(self):
        self.assertAlmostEqual(scientific_calc.power(4, -1), 0.25)


class TestLogarithm(unittest.TestCase):

    def test_natural_log(self):
        self.assertAlmostEqual(scientific_calc.logarithm(math.e), 1.0)

    def test_base_10(self):
        self.assertAlmostEqual(scientific_calc.logarithm(1000, 10), 3.0)

    def test_base_2(self):
        self.assertAlmostEqual(scientific_calc.logarithm(16, 2), 4.0)

    def test_log_of_one(self):
        self.assertAlmostEqual(scientific_calc.logarithm(1), 0.0)

    def test_non_positive_raises(self):
        with self.assertRaises(ValueError):
            scientific_calc.logarithm(-1)

    def test_base_one_raises(self):
        with self.assertRaises(ValueError):
            scientific_calc.logarithm(10, 1)


class TestTrigonometry(unittest.TestCase):

    def test_sine_zero(self):
        self.assertAlmostEqual(scientific_calc.sine(0), 0.0)

    def test_sine_90(self):
        self.assertAlmostEqual(scientific_calc.sine(90), 1.0)

    def test_cosine_zero(self):
        self.assertAlmostEqual(scientific_calc.cosine(0), 1.0)

    def test_cosine_180(self):
        self.assertAlmostEqual(scientific_calc.cosine(180), -1.0)

    def test_tangent_zero(self):
        self.assertAlmostEqual(scientific_calc.tangent(0), 0.0)

    def test_tangent_45(self):
        self.assertAlmostEqual(scientific_calc.tangent(45), 1.0)

    def test_tangent_90_raises(self):
        with self.assertRaises(ValueError):
            scientific_calc.tangent(90)


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(scientific_calc.factorial(0), 1)

    def test_five(self):
        self.assertEqual(scientific_calc.factorial(5), 120)

    def test_ten(self):
        self.assertEqual(scientific_calc.factorial(10), 3628800)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            scientific_calc.factorial(-3)

    def test_float_raises(self):
        with self.assertRaises(TypeError):
            scientific_calc.factorial(2.5)


if __name__ == '__main__':
    unittest.main()