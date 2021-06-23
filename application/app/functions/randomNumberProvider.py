import os
import random

class randomNumberProvider:
    def __init__(self, total, unitTypeCount):
        random.seed(os.urandom(16))
        self.total = total
        self.unitTypeCount = unitTypeCount

    def ggRand(self):
        """ provides a random number between min and max """
        if self.total < self.unitTypeCount:
            raise Exception("Your desired army is smaller than the number of service branches.")
        if self.unitTypeCount == 0:
            raise Exception("Random numbers starved.")
        if self.unitTypeCount == 1:
            return self.total
        if self.unitTypeCount == self.total:
            self.total -= 1
            self.unitTypeCount -= 1
            return 1
        else:
            result = random.randint(1, self.total-self.unitTypeCount+1)
            self.total -= result
            self.unitTypeCount -= 1
            return result
