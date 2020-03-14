from numpy import absolute, asarray
from StatisticsFunctions.Mean import Mean

class MeanDeviation:
   @staticmethod
   def meanDeviation(data):
      return Mean(absolute(asarray(data) - Mean(data)))