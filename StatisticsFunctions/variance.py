from numpy import absolute, asarray
from StatisticsFunctions import Mean

class Variance:
    @staticmethod
    def variance(data):
        return Mean.Mean(absolute(asarray(data) - Mean.Mean(data))**2)