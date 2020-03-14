from RandomGenerator.SelectWithSeed import SelectWithSeed

class PopulationProportion():
    @staticmethod

    def proportion(sd, data, rnge):
        data2 = SelectWithSeed.pickItem(sd, data, rnge)
        proportion = len(data2)/len(data)
        return proportion