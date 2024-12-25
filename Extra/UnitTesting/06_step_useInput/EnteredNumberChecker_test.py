import unittest
from unittest.mock import patch
from EnteredNumberChecker import EnteredNumberChecker


class TestEnteredNumberChecker(unittest.TestCase):
    def setUp(self):
        self.target: EnteredNumberChecker = EnteredNumberChecker()

    @patch("builtins.input", return_value="10")
    def test_GetNumberFromInput(self):
        result: int = self.target.GetNumberFromInput()
        self.assertEqual(10, result)


if __name__ == "__main__":
    unittest.main()
