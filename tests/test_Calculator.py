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

    def test_division(self):
        test_data = CsvReader("../tests/data/Unit Test Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.dividing(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("../tests/data/Unit Test Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqr(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqr_root(self):
        test_data = CsvReader("../tests/data/Unit Test Square Root.csv").data
        for row in test_data:
            result = round(float(row['Result']), 8)
            self.assertEqual(self.calculator.sqr_root(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_zero_division_error(self):
        self.assertRaises(ZeroDivisionError, self.calculator.dividing(0, 1))

    if __name__ == '__main__':
        unittest.main()
