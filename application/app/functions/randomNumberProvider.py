import os
import random
from app.config.settings import GameSettings as gs

class randomNumberProvider:
    """
        use the cryptographicly secure os.urandom() function to seed the random number generator upon creation.
    """
    def __init__(self, total, unitTypeCount):
        random.seed(os.urandom(16))
        self.total = total
        self.unitTypeCount = unitTypeCount
        self.sigma = 0

        self.factors = [lambda f : random.randint(1,9) for u in gs.serviceBranches]
        self.sigma = sum(self.factors)
        self.ratios = [lambda r : f/self.sigma for f in self.factors]

    def ggRand(self):
        if self.total < self.unitTypeCount:
            raise Exception("Your desired army is smaller than the number of service branches.")#
        if self.unitTypeCount == 0:
            raise Exception("Random numbers starved.")
        if self.unitTypeCount == self.total:
            self.total -= 1
            self.unitTypeCount -= 1
            return 1

        if self.sum < self.total:
            return self.randi()
        else:
            return self.randr()

    def randi(self):
        """ provides a random number according to the remaining number of unity types and total number of desired troops """
        if self.unitTypeCount == 1:
            return self.total
        else:
            result = random.randint(1, self.total-self.unitTypeCount+1)
            self.total -= result
            self.unitTypeCount -= 1
            return result

    def randr(self):
        print("WIP")
