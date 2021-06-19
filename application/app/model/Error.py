from app.model.JSONable import JSONable


class Error(JSONable):
    def __init__(self, code, message):
        super().__init__()
        self.status = code
        self.errorMessage = ErrorMessage(message)

class ErrorMessage(JSONable):
    def __init__(self, message):
        super().__init__()
        self.type = message.name
        if isinstance(message.description, str):
            self.description = message.description
        else:
            self.description = message.description.args[0]


