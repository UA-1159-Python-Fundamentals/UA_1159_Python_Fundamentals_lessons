class Human():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Human({self.name})"

    def welcome_message(self):
        return f"Hola, amigo {self.name}!"

    @classmethod
    def is_homosapiens(cls):
        return "Homo sapiens"

    @staticmethod
    def message():
        return "An arbitrary message"
