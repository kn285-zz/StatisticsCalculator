from numpy import absolute, asarray
from StatisticsFunctions.mean import Mean

class MeanDeviation:
   @staticmethod
   def meanDeviation(data):
      return Mean.Mean(absolute(asarray(data) - Mean.Mean(data)))