from MathOperations.root import root
from StatisticsFunctions.variance import Variance

class StandardDeviation:
   @staticmethod
   def standardDeviation(data):
      return root.root(Variance.variance(data), 2)