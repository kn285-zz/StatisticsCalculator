from StatisticsFunctions.Mean import Mean
from StatisticsFunctions.StandardDeviation import StandardDeviation
from RandomGenerator.PickSeedList import PickSeedList
from MathOperations.division import Division


class zscore():
    @staticmethod

    def zscore(sd, data):
        X = PickSeedList.pickSeed(sd, data)
        meanData = Mean(data)
        sd = StandardDeviation.standardDeviation(data)
        z = Division.divide(X-meanData, sd)
        return z