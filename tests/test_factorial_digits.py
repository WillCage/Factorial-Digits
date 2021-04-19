import unittest
import factorial_digits as fd

class TestFactorialDigits(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(fd.calculate_sum_of_digits(0), 0)
        self.assertEqual(fd.calculate_sum_of_digits(1), 1)
        self.assertEqual(fd.calculate_sum_of_digits(2), 2)
        self.assertEqual(fd.calculate_sum_of_digits(10), 1)
        self.assertEqual(fd.calculate_sum_of_digits(11), 2)
        self.assertEqual(fd.calculate_sum_of_digits(1234567890), 45)

    def test_sum_of_factorial_digits(self):
        self.assertEqual(fd.calculate_sum_of_factorial_digits(1), 1)
        self.assertEqual(fd.calculate_sum_of_factorial_digits(10), 27)
        self.assertEqual(fd.calculate_sum_of_factorial_digits(100), 648)
        self.assertEqual(fd.calculate_sum_of_factorial_digits(1000), 10539)
        self.assertEqual(fd.calculate_sum_of_factorial_digits(10000), 149346)

    def test_values(self):
        self.assertRaises(ValueError, fd.calculate_sum_of_factorial_digits, -1)
        self.assertRaises(ValueError, fd.calculate_sum_of_factorial_digits, -2)

    def test_types(self):
        self.assertRaises(TypeError, fd.calculate_sum_of_factorial_digits, 3+5j)
        self.assertRaises(TypeError, fd.calculate_sum_of_factorial_digits, True)
        self.assertRaises(TypeError, fd.calculate_sum_of_factorial_digits, "factorial")
