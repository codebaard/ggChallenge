from app.model.JSONable import JSONable
from app.model.Troop import Troop
from app.config.settings import GameSettings
from app.functions.randomNumberProvider import randomNumberProvider

class Army(JSONable):
    """
        Army data-model with a total size property and a list of Troop-members.
    """
    def __init__(self, totalSize):
        super().__init__()
        self.total = int(totalSize)
        self.troops = []

    def populate(self):
        """
            Creates a new randomNumberProvider object with the parameters of army-size and unittype-count
            this randomNumberProvider object is subsequently used to populate the troop-list
        """
        rnd = randomNumberProvider(self.total, len(GameSettings.serviceBranches))
        for branch in GameSettings.serviceBranches:
            self.troops.append(Troop(branch, rnd.ggRand()))



