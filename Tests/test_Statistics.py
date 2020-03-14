import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 38.95)

    def test_median_calculator(self):
        med = self.statistics.median(self.testData)
        self.assertEqual(med, 27.5)

    def test_mode_calculator(self):
        theMode = self.statistics.mode(self.testData)
        self.assertEqual(theMode, 2)

if __name__ == '__main__':
    unittest.main()