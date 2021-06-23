from app.model.JSONable import JSONable

class Troop(JSONable):
    """
        Troop data-model with a name and count property.
    """
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count
