import unittest

from src.calculator.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator1 = Calculator()
        self.assertIsInstance(calculator1, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)



