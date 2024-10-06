import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 3), 6)
        self.assertEqual(self.calc.add(-1, 6), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 6), 2)
        self.assertEqual(self.calc.subtract(8, 9), -1)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(0, 7), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(10, 0), "Error: Cannot divide by zero.")

