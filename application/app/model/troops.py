import functions.randomNumberProvider as rnd
from model.JSONable import JSONable

class Army(JSONable):

    def __init__(self, totalSize):
        self.total = totalSize
        self.troops = {}

    def populate(self, func):
        spr = Troop("spearmen", 0)
        swd = Troop("swordsmen", 0)
        arc = Troop("archers", 0)

        print(spr.name)

        if func == 'flat':
            spr.count, swd.count, arc.count = rnd.ggRand(self.total)
        else:
            spr.count, swd.count, arc.count = rnd.ggRandn(50 ,self.total)

        self.troops = [spr, swd, arc]
        

class Troop(JSONable):
    def __init__(self, name, count):
        self.name = ""
        self.count = 0

