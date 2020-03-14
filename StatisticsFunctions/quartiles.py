import numpy

class Quartiles:

    @staticmethod
    def quartiles(data):
        a = numpy.quantile(data,0.25)
        b = numpy.quantile(data,0.5)
        c = numpy.quantile(data,0.75)

        return [a, b, c]
