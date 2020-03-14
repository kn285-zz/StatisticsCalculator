from scipy.stats import sem, t

from PopulationSamplingFunctions.ConfidenceIntervalPop import ConfidenceIntervalPop
from PopulationSamplingFunctions.SimpleSampling import SimpleSampling


class ConfidenceInterval(ConfidenceIntervalPop):
    @staticmethod
    def confidenceInterval(conf, data, sd, higher):
        sample = SimpleSampling.generateSampling(sd, data, higher)
        return ConfidenceIntervalPop.confidenceIntervalPop(conf, sample)