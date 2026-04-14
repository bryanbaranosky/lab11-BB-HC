# https://github.com/bryanbaranosky/lab11-BB-HC.git
# Partner 1: Hunter Coffman
# Partner 2: Bryan Baranosky

from calculator import *
import unittest

class TestCalculator(unittest.TestCase):

    # -------- Partner 2 --------
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 10), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)

    # -------- Partner 1 --------
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(0, 5), 0)
        self.assertEqual(mul(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 0), 0)
        self.assertEqual(div(4, 8), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)


if __name__ == "__main__":
    unittest.main()