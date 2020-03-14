from StatisticsFunctions.Covariance import Covariance
from StatisticsFunctions.StandardDeviation import StandardDeviation
from RandomGenerator.SelectWithSeed import SelectWithSeed


class SampleCorrelation():
    @staticmethod

    def correlation(sd, a, b):
        sampleA = SelectWithSeed.pickItem(sd, a, 10)
        sampleB = SelectWithSeed.pickItem(sd, b, 10)

        cov = Covariance.covariance(sampleA, sampleB)
        stdDevA = StandardDeviation.standardDeviation(sampleA)
        stdDevB = StandardDeviation.standardDeviation(sampleB)
        return cov/(stdDevA*stdDevB)