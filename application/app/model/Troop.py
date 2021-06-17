from app.model.JSONable import JSONable

class Troop(JSONable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count
