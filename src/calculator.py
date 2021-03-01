from src.operator.addition import addition
from src.operator.subtraction import subtraction
from src.operator.multiplication import multiplication
from src.operator.division import division
from src.operator.square import square
from src.operator.square_root import square_root


class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result = x
        pass

    @staticmethod
    def adding(self, a, b):
        self.result = addition(a, b)
        return self.result

    @staticmethod
    def subtracting(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    @staticmethod
    def multiplying(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    @staticmethod
    def dividing(self, a, b):
        self.result = division(a, b)
        return self.result

    @staticmethod
    def sqr(self, a):
        self.result = square(a)
        return self.result

    @staticmethod
    def sqr_root(self, a):
        self.result = square_root(a)
        return self.result
