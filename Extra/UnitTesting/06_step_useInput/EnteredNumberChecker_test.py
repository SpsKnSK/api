import unittest
from unittest.mock import patch
from enteredNumberChecker import EnteredNumberChecker


class TestEnteredNumberChecker(unittest.TestCase):
    def setUp(self):
        self.target: EnteredNumberChecker = EnteredNumberChecker()

    @patch("builtins.input", return_value="10")
    def test_GetNumberFromInput_correctNumberFormat(self, input):
        result: int = self.target.GetNumberFromInput()
        self.assertEqual(10, result)

    @unittest.expectedFailure
    @patch("builtins.input", return_value="text")
    def test_GetNumberFromInput_enteredText_expectingException(self, input):
        self.target.GetNumberFromInput()

    @patch("builtins.input", return_value="text")
    def test_GetNumberFromInput_enteredText_expectingException_1(self, input):
        with self.assertRaises(Exception):
            self.target.GetNumberFromInput()


if __name__ == "__main__":
    unittest.main()
