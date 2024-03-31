import random
class Ghost(object):
    collos_list = ( "white", "yellow", "purple", "red")
    def __init__(self):
        self.color = Ghost.collos_list[random.randint(0,len(Ghost.collos_list)-1)]