from numpy.random import seed
from RandomGenerator.SelectItemList import SelectItemList

class PickSeedList():
    @staticmethod

    def pickSeed(sd, lst):
        seed(sd)

        return SelectItemList.pickItem(lst)