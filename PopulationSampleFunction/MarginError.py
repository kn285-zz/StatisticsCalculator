from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Zscore import Zscore


class MarginError():
    @staticmethod

    def margin(sd, data):
        z_score = Zscore.zscore(sd, data)
        stdDev = StandardDeviation.standardDeviation(data)
        return z_score * stdDev