from StatisticFunctions.Zscore import Zscore
from PopulationSamplingFunctions.MarginError import MarginError
from StatisticFunctions.StandardDeviation import StandardDeviation
from MathOperations.exponentiation import Exponentiation

class SampleSizeKnownPop():
    @staticmethod

    def sampleSize(sd, data):

        e = MarginError.margin(sd, data)
        stdDev = StandardDeviation.standardDeviation(data)
        val = (1.96 * stdDev) / e
        sample = Exponentiation.exponent(val, 2)

        return sample