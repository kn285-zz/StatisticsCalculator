from numpy.random import seed
from numpy.random import randint

class rand_num:
    @staticmethod
    def random_int_generator(low, high, num, seed_num):
        if seed_num is None:
            data = randint(low, high, num)
            return data
        seed(seed_num)
        data = randint(low, high, num)
        return data