from app.model.JSONable import JSONable
from app.model.Troop import Troop
from app.config.settings import GameSettings
from app.functions.randomNumberProvider import randomNumberProvider

class Army(JSONable):
    def __init__(self, totalSize):
        super().__init__()
        self.total = totalSize
        self.troops = []

    def populate(self):
        rnd = randomNumberProvider(self.total)
        for branch in GameSettings.serviceBranches:
            self.troops.append(Troop(branch, rnd.ggRand()))

        #print(self.troops)



