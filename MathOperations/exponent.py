import math;

class exponent:
    @staticmethod
    def power(base, exponent=None):
        if (isinstance(base, list)):
            return Exponentiation.powerList(base)
        return math.pow(base,exponent)

    @staticmethod
    def powerList(valueList):
        result = 1
        for element in valueList:
            result = Exponentiation.power(element, result)
        return result