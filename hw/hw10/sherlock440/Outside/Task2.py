import random

class Ghost():
    def __init__(self):
        self.color = random.choice(("white", "yellow", "purple", "red"))


a = Ghost()
print(a.color)
