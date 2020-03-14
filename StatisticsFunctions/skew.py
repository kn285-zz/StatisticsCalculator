import scipy.stats

class Skew:
    @staticmethod
    def skewness(data):
        return scipy.stats.skew(data)