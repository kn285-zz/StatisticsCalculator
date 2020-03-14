import numpy as np


class Covariance():
    @staticmethod

    def covariance(a, b):

        return np.cov(a, b)[0, 1]