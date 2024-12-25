import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.target: Calculator = Calculator()

    @unittest.expectedFailure
    def test_divideByZero(self):
        self.target.divide(1, 0)

    def test_divideByZero_1(self):
        with self.assertRaises(Exception):
            self.target.divide(1, 0)


if __name__ == "__main__":
    unittest.main()
