from random import choice

class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]
    
    def __init__(self):
        self.color = choice(__class__.colors)