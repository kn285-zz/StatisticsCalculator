import unittest
from StatisticsFunctions.mean import Mean
from StatisticsFunctions.median import Median
from StatisticsFunctions.mode import mode
from StatisticsFunctions.MeanDeviation import MeanDeviation
from StatisticsFunctions.StandardDeviation import StandardDeviation
from StatisticsFunctions.variance import Variance
from StatisticsFunctions.quartiles import Quartiles
from StatisticsFunctions.skew import Skew
from Random.Random import getRandomNums
from StatisticsFunctions.Covariance import Covariance
from StatisticsFunctions.zscore import zscore
from StatisticsFunctions.SampleCorrelation import SampleCorrelation
from StatisticsFunctions.PopulationCorrelation import PopulationCorrelation
from StatisticsFunctions.PopulationProportion import PopulationProportion

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)
        self.testData2 = getRandomNums(3, 1, 100, 20)

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(38.95, Mean.mean(self.testData))

    def test_StatisticFunctions_Median(self):
        self.assertEqual(27.5, Median.median(self.testData))

    def test_StatisticFunctions_Mode(self):
        self.assertEqual(2, mode.mode(self.testData))

    def test_StatisticFunctions_MeanDeviation(self):
        self.assertEqual(26.740000000000002, MeanDeviation.meanDeviation(self.testData))

    def test_StatisticFunctions_Variance(self):
        self.assertEqual(844.0474999999999, Variance.variance(self.testData))

    def test_StatisticFunctions_StandardDeviation(self):
        self.assertEqual(29.052495589880053, StandardDeviation.standardDeviation(self.testData))

    def test_StatisticFunctions_Quartiles(self):
        self.assertEqual([12.75, 27.5, 72.25], Quartiles.quartiles(self.testData))

    def test_StatisticFunctions_Skewness(self):
        self.assertEqual(0.3265989606653176, Skew.skewness(self.testData))

    def test_StatisticFunctions_Covariance(self):
        self.assertEqual(-188.54736842105262, Covariance.covariance(self.testData, self.testData2))

    def test_StatisticsFunctions_ZScore(self):
        self.assertEqual(-0.7555289, zscore.zscore(self.testData))

    def test_StatisticFunctions_PopulationCorrelation(self):
        self.assertEqual(-0.22499088742463133, PopulationCorrelation.popCor(self.testData, self.testData2))

    def test_StatisticFunctions_PopulationProportion(self):
        self.assertEqual(0.2, PopulationProportion.proportion(3, self.testData, 4))

    def test_StatisticFunctions_SampleCorrelation(self):
        self.assertEqual(-0.4110789854375375, SampleCorrelation.correlation(3, self.testData, self.testData2))


