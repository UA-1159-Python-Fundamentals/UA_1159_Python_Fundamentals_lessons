class BlackjackException(Exception):
    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description
