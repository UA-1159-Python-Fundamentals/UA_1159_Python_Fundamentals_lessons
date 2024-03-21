# class MyClass:
#     """ToTo DocString"""

# # print(MyClass.__doc__)

# # help(MyClass)


# m1 = MyClass()
# m2 = MyClass()
# i = 10
# i = int(10)
# print(m1)
# print(m2)
# print(id(m2))
# print(str(m2)[str(m2).find("0x")+2:-1], " => ", int(str(m2)[str(m2).find("0x")+2:-1], 16))


# class MyClass:
#     cm = []
#     ci = 10

#     def __init__(self):
#         self.im = [15, 16]
#         self.ii = "text"


# m1 = MyClass()
# m2 = MyClass()
# print(dir(m1))
# print(m1.cm, m1.ci, m1.im, m1.ii, m1.__dict__)
# print(m2.cm, m2.ci, m2.im, m2.ii, m2.__dict__)
# MyClass.ci = 88888
# m1.cm.append(99)
# m1.ci = "Error"
# m1.im.append("test1")
# m2.cm = [1,2,3]
# print(m1.cm, m1.ci, m1.im, m1.ii, m1.__dict__, m1.__class__.ci)
# print(m2.cm, m2.ci, m2.im, m2.ii, m2.__dict__, m2.__class__.cm)

# print(m2)

# print(dir(MyClass))
# print(MyClass.__dict__.keys())
# print(dir(m1))
# print(m1.__dict__.keys())
# print(m1.__dict__)


# class User:
#     def __init__(self, name="no_neme", age = 0, sex="no_data"):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __str__(self):
#         return f"name:{self.name} age:{self.age} sex:{self.sex}"
#     def print(self):
#         print("name:", self.name)
#         print("age", self.age)
#         print("sex", self.sex)
# user1 = User()
# user2 = User("Anna", "16", "women")
# print(user1)
# print(user2)
# print(User.__dict__)
# print(user1.__dict__)
# print(type(User))
# print(type(user1))
# user1.print()
# user2.print()
# # User.print()#error
# User.print(user1)
# my_f = User.print
# my_f(user2)
# my_obj = lambda x:x
# print(my_obj)
# my_obj.name = "name"
# my_obj.age = "ageeeee"
# my_obj.sex = "sex"
# my_obj.h = 180
# my_f(my_obj)

# def f(obj, new_age):
#     obj.age = new_age

# print(my_obj.age)
# f(my_obj, 99)
# print(my_obj.age)

# User.set_age = f
# print(user1)
# user1.set_age(77)
# print(user1)


# class Point:

#     count = 0

#     def __init__(self, x=0, y=0):

#         print("Point.__init__")
#         self.x = x
#         self.y = y
#         Point.count +=1

#     def __str__(self):
#         return f"x:{self.x} y:{self.y}"

#     def __repr__(self):
#         return f"({self.x},{self.y})"

#     # def __del__(self):
#     #     print("del", self)

#     def dist(self, point):
#         return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5

#     def add(self, other):
#         point = Point()
#         point.x = self.x + other.x
#         point.y = self.y + other.y
#         return point

#     def __add__(self, other):
#         point = Point()
#         point.x = self.x + other.x
#         point.y = self.y + other.y
#         return point

#     def __lt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# # p1 = Point()
# # p2 = Point(1)
# # p3 = Point(1, 2)
# # p4 = Point(2, 3)

# # points = [p1, p2, p3]
# # print("points:", points)
# # del p3
# # print(f"dist {p1}->{p2} = ", p1.dist(p2))
# # s = str(p1)

# # p5 = p2.add(p4)
# # print(p5)

# # p6 = p5 + p4
# # print(p6)
# # points.append(p5)
# # points.append(p6)
# # print(points)
# # points.sort()
# # print(points)
# # print(p6 == p2)

# # p7 = Point(p6.x, p6.y)
# # print(p6, p7)
# # print(p7 == p6)


# class PointColor(Point):


#     def __init__(self, x=0, y=0, color=None):
#         print("PointColor.__init__")
#         super().__init__(x, y)
#         self.color = color

#     def __str__(self):
#         return f"x:{self.x} y:{self.y} color:{self.color}"


# p3 = Point(1, 2)
# p4 = Point(2, 3)
# pc1 = PointColor(3, 4)
# pc2 = PointColor(9, 5, "red")
# print(p3)
# print(pc1)
# points = [pc2, p4, pc1, p3]
# print(points)
# for point in points:
#     print(point)

# print(isinstance(p4, Point))
# print(isinstance(p4, PointColor))
# print(isinstance(pc1, Point), type(pc1) is Point)
# print(isinstance(pc1, PointColor), type(pc1) is PointColor)

# print(Point.count)


# def stat():
#     print("sta")


# class Point:
#     count = 0
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         self.count_up()
#         print(f"create point_{self.count} <{self.x}, {self.y}>")

#     def print(self):
#         print(self)

#     @classmethod
#     def count_up(cls):
#         cls.count += 1

#     @staticmethod
#     def stat():

#         print("sta")


# p = Point()
# p.print()
# p = Point()
# p.print()
# p = Point()
# p.print()
# p.count_up()
# print(p.count)
# # Point.print() #Error
# Point.count_up()
# print(p.count)
# p = Point()
# p.print()
# Point.stat()
# p.stat()


# class Encapsulation(object):
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#     def print(self):
#         print(self.__dict__)
#         print(self.public)
#         print(self._protected)
#         print(self.__private)


# e = Encapsulation(1,2,3)

# print(e.public)
# print(e._protected)
# e.print()
# # print(e.__private)
# print(e.__dict__)
# print(e._Encapsulation__private)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __repr__(self):
#         return f"({self.__x},{self.__y})"

#     def get_x(self):
#         print("get_x")
#         return self.__x

#     @property
#     def y(self):
#         print("get_y")
#         return self.__x

#     def set_x(self, x):
#         print("set_x")
#         if type(x) in (int, float):
#             self.__x = x
#         else:
#             print("bed value")

#     x = property(get_x, set_x)

#     @y.setter
#     def y(self, x):
#         print("set_x")
#         if type(x) in (int, float):
#             self.__x = x
#         else:
#             print("bed value")


# p = Point(8, 33)
# # print(p)
# # # print(p.__x)#error
# # print(p.get_x())
# # p.set_x(99)
# # print(p.get_x(), p)
# # p.set_x("99")

# print(p.x)
# p.x = 55
# print(p)
# print(p.y)
# p.y = 777
# p.y = "a"
# print(p)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def print(self):
#         print(f"({self.__x},{self.__y})")

#     def print(self, text=None):
#         print(f"({self.__x},{self.__y})" + (text if text else "__"))


# p = Point(8, 33)
# p.print()
# p.print("aa")
