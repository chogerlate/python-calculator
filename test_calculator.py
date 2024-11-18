import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for addition
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -2), -5)

    # Test cases for subtraction
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    # Test cases for multiplication
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    # Test cases for division
    def test_divide_whole_number(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):  # Expect an exception
            self.calc.divide(10, 0)

    # Test cases for modulo
    def test_modulo_with_remainder(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_without_remainder(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

if __name__ == '__main__':
    unittest.main()
