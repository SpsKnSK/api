import unittest
from parameterized import parameterized  # pip install parameterized
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.target: Calculator = Calculator()

    @parameterized.expand(
        [
            ("positive_integers", 1, 2, 3),
            ("negative_integers", -1, -2, -3),
            ("mixed_integers", -1, 2, 1),
            ("floats", 1.5, 2.5, 4.0),
            ("zero", 0, 0, 0),
            ("large_numbers", 1000000, 2000000, 3000000),
        ]
    )
    def test_add(self, numberType: str, a: float, b: float, expected: float) -> None:
        result: float = self.target.add(a, b)
        self.assertEqual(result, expected, msg=f"Working with: {numberType}")


if __name__ == "__main__":
    unittest.main()
