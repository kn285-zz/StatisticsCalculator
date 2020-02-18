class Squareroot:

    @staticmethod
    def squareroot(base):
        if isinstance(base, list):
            return Squareroot.squareList(base)
        return base ** 0.5

    @staticmethod
    def squareList(sqrtList):
        for value in sqrtList:
            result = Squareroot.squareroot(value)

        return result