import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.target: Calculator = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.target.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(self.target.add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.target.add(1, -2), -1)
        self.assertEqual(self.target.add(-1, 2), 1)


if __name__ == "__main__":
    unittest.main()
