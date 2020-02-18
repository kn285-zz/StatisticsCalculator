import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.squareroot import Squareroot
from MathOperations.square import Square



class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_diff_list(self):
        sublist = [8, 4, 2]
        self.assertEqual(2, Subtraction.difference(sublist))

    def test_MathOperations_multi_list(self):
        multilist = [2, 2, 2]
        self.assertEqual(8, Multiplication.multiply(multilist))

    def test_MathOperations_divide_list(self):
        dividend = 16
        divisor = 2
        result = Division.divide(dividend, divisor)
        self.assertEqual(8, result)

    def test_MathOperations_squareroot_list(self):
        sqrtList=[16]
        self.assertEqual(4, Squareroot.squareroot(sqrtList))
        
    def test_MathOperations_square_list(self):
        sqList=[2]
        self.assertEqual(4, Square.square(sqList))




if __name__ == '__main__':
    unittest.main()