import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.target: Calculator = Calculator()


if __name__ == "__main__":
    unittest.main()
