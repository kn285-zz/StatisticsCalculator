from numpy import absolute, asarray
from StatisticsFunctions.mean import Mean

class Variance:
    @staticmethod
    def variance(data):
        return Mean.mean(absolute(asarray(data) - Mean.mean(data))**2)