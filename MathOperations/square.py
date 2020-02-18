class Square:

    @staticmethod
    def square(base):
        if isinstance(base, list):
            return Square.squareList(base)
        return base * base

    @staticmethod
    def squareList(sqList):
        for value in sqList:
            result = Square.square(value)

        return result