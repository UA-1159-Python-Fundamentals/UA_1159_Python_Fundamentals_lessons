from logconfig import logging

class PointError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr("PointError:" + self.data)



class Point:

    def __init__(self, x=0, y=0):

        if type(x) not in (int, float):
            raise PointError(f"x not number {x}")
        if type(y) not in (int, float):
            raise ValueError(f"y not number {y}")
        self.x = x
        self.y = y
        logging.info(f"create point{self.__repr__()}")

    def __str__(self):
        return f"x:{self.x} y:{self.y}"

    def __repr__(self):
        return f"({self.x},{self.y})"

    # def __del__(self):
    #     print("del", self)

    def dist(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5

    def add(self, other):
        point = Point()
        point.x = self.x + other.x
        point.y = self.y + other.y
        return point

    def __add__(self, other):
        point = Point()
        point.x = self.x + other.x
        point.y = self.y + other.y
        return point

    def __lt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y