# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):  # MUST start with test_
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):  # MUST start with test_
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(8, 0))  # division by zero case
