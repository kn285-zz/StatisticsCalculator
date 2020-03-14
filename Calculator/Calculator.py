from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.square import Square
from MathOperations.root import root
from MathOperations.logarithm import logarithm

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiplication(self, a, b):
        self.Result = Multiplication.multiply(a,b)
        return self.Result

    def Division(self, a, b):
        self.Result = Division.divide(a,b)
        return self.Result

    def Square(self, a, b):
        self.Result = Square.square(a,b)
        return self.Result

    def nthroot(self, a, b):
        self.Result = root.root(a, b)
        return self.Result

    def log(self, a, b):
        self.Result = logarithm(a,b)
        return self.Result