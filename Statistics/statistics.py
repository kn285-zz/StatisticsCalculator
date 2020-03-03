from Calculator.Calculator import Calculator
from Statistics.mean import Mean

from MathOperations.rand_num import rand_num;

class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result


    def Random_int_nums(self, a, b, c, d):
        self.Result = rand_num.random_int_generator(a,b,c,d)
        return self.Result