from numpy.random import seed
from RandomGenerator.SelectWithoutSeed import SelectWithoutSeed

class SelectWithSeed():
    @staticmethod
    def pickItem(sd, lst, rnge):
        seed(sd)
        lst2 = SelectWithoutSeed.pickItem(lst, rnge)
        return lst2