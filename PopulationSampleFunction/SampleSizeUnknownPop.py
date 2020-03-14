from StatisticFunctions.Zscore import Zscore
from PopulationSamplingFunctions.MarginError import MarginError
from MathOperations.exponentiation import Exponentiation

class SampleSizeUnkownPop():
    @staticmethod

    def sampleSize(sd, data, percentage):
        z = Zscore.zscore(sd, data)
        e = MarginError.margin(sd, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = Exponentiation.exponent(val, 2) * p * q

        return sample