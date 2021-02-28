import unittest, csv

from src.calculator import Calculator
from src.CsvReader.CsvReader import CsvReader


class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("../tests/data/Unit Test Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.adding(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader("../tests/data/Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtracting(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("../tests/data/Unit Test Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiplying(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    if __name__ == '__main__':
        unittest.main()
