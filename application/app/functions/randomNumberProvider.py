import os
import random

class randomNumberProvider:
    def __init__(self, total):
        random.seed(os.urandom(10))
        self.total = total

    def ggRand(self):
        """ provides a random number between min and max """
        #random.randint(min, max)
        return 42
