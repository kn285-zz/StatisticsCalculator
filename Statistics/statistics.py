from Calculator.Calculator import Calculator
from Statistics.mean import Mean
from Statistics.mode import mode
from Statistics.median import Median

class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result

    def median(self, data):
        self.result = Median.median(data)
        return self.result

    def mode(self, data):
        self.result = mode.mode(data)