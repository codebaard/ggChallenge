import json
from JSONable import JSONable
from app.functions import randomNumberProvider as rnd

class Army(JSONable):

    def __init__(self, totalSize):
        self.total = totalSize
        self.troops = {}

    def populate(func):
        if func == 'flat':
            rnd.ggRand()
        else:
            rnd.ggRandn()
        

class Troop(JSONable):
    def __init__(self, name, count):
        self.count = 0
        self.name = ""
