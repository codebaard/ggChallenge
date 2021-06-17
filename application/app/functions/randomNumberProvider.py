import os
import random

class randomNumberProvider:
    def __init__(self, total, unitTypeCount):
        random.seed(os.urandom(10))
        self.total = total
        self.unitTypeCount = unitTypeCount

    def ggRand(self):
        """ provides a random number between min and max """
        if self.total < self.unitTypeCount:
            raise Exception("Your desired army is smaller than the number of service branches.")

        result = random.randint(self.unitTypeCount, self.total)
        self.total -= result
        self.unitTypeCount -= 1
        return result
