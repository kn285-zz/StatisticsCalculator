class Multiplication:

    @staticmethod
    def multiply(multiplier, multiplicand=None):
        if isinstance(multiplier, list):
            return Multiplication.multiplyList(multiplier)
        return multiplier * multiplicand

    @staticmethod
    def multiplyList(multilist):
        result = 1
        for value in multilist:
            result = Multiplication.multiply(result, value)

        return result