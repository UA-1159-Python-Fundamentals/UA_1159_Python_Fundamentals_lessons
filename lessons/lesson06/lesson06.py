# #list


# l = list()

# print(type(l), l)

# # l = list(1)#error
# l = list("qwerty")

# print(type(l), l)

# l = []

# print(type(l), l)

# l = [1, 2, "3,4" ,5, [1,2,3,[1,222,3]]]

# print(type(l), l)

# print(l[2])
# print(l[4][3])
# print(l[4][3][1])
# print(l[-1][2])
# print(l[1:4])

# print([method for method in dir(list) if not method.startswith("_")])

# l = []

# l.append(1)
# print(type(l), l)
# l.append([1,2])
# print(type(l), l)
# l.append("test")
# print(type(l), l)

# # l.extend(123)#error
# l.extend((1,2,3))
# print(type(l), l)
# l.append("test")
# l.extend("test")
# print(type(l), l)
# print(id(l), l)
# l.clear()
# print(id(l), l)
# l = []
# print(id(l), l)


# d1 = [22, 33]
# d2 = [99, 88]

# l = [1, 2, 3, d1, d2]
# print(id(d2))
# print(id(l[4]))

# print(l)
# d1.clear()
# print(l)
# d2 = []
# print(l)
# d1.append(100)
# d2.append(200)
# print(l, d1, d2)
# l.clear()
# print(l, d1, d2)



# l = [1, 2, 3, d1, d2]
# r = l[4]
# print(r)
# print(id(r))

# d1 = [22, 33]
# d2 = [99, 88]

# l = [1, 2, 3, d1, d2]

# l1 = l.copy()
# # l1 = l[:]
# print(id(l), l)
# print(id(l1), l1)
# l[0] = 100
# l1[1] = 200
# print(id(l), l)
# print(id(l1), l1)
# l[3][0]="a"
# l1[4][1]="b"
# print(id(l), l)
# print(id(l1), l1)

# d1 = [22, 33]
# d2 = [99, 88]

# l = [1, 2, 3, d1, d2]
# import copy
# l1 = copy.deepcopy(l)
# # l1 = l[:]
# print(id(l), l)
# print(id(l1), l1)
# l[0] = 100
# l1[1] = 200
# print(id(l), l)
# print(id(l1), l1)
# l[3][0]="a"
# l1[4][1]="b"
# print(id(l), l)
# print(id(l1), l1)

# print(d1.__sizeof__())

# l = [1, 2, 3, 1,2,3,4,1,"Q",1,2,3,4,"Q"]
# print(l.count(1))
# print(l.count(3))
# print(l.count(9))
# print(l.index(3))
# # print(l.index(9))#ValueError: 9 is not in list
# print(l.index(3, 4))
# print(l.index(3, 4, 100))

# print(l)
# l.insert(2, "Q")
# l.insert(552, "W")
# print(l)
# t = l.pop()
# print(t, l)
# t = l.pop(10)
# print(t, l)
# t = l.remove(2)
# t = l.remove("Q")
# print(t, l)

# # t = l.remove("q") #ValueError: list.remove(x): x not in list

# n = 3
# while n in l:
#     l.remove(n)
# print(l)


# d1 = [22, 33]
# d2 = [99, 88]

# l = [1, 2, 3, d1, d2]

# # # del d1
# print(l)
# # print(d1)
# del l[3]
# print(l)
# print(d1)
# del l[2]

# print(id(d1))
# print(id(l[3]))

# print(l)
# l.reverse()
# print(l)
# print(list(reversed(l)))
# print(l)
# print(l[::-1])
# l = [1, 2, 3, 1,2]

# print(sorted(l))
# # l.sort()
# print(l)

# def s(element):
#     if type(element) is list:
#         return sum(element)
#     if type(element) is str:
#         k = 0
#         for i in element:
#             k += ord(i)
#         return k
#     else:
#         return element


# d1 = [22, 33]
# d2 = [-99, 100]

# l = [1, 2, 3, d1, d2, "s", ]
# l.sort(key=s)
# print(l)

# l = ["aa", "a", "e", ]
# l.sort()
# print(l)

# l = [["aa1", "a", "e3", ], ["aa3", "a", "e3", ], ["aa2", "a", "e3", ]]
# l.sort()

# print(l)

# l = [(i, j) for i in range(3) for j in range(3) if i!=j]
# print(l)

# l = []
# for i in range(3):
#     for j in range(3):
#          if i!=j:
#               l.append((i, j))
# print(l)


# print([method for method in dir(tuple) if not method.startswith("_")])

# t = (1,2,3)
# # t[1]=33#error

# print(max(t))

# t= tuple()

# print(type(t), t)
# t= tuple("dsbfkahsd")
# print(type(t), t)
# t=()
# print(type(t), t)
# t=(1,2,3,"s")
# print(type(t), t)

# t=(1)
# print(type(t), t)
# t=(1,)
# print(type(t), t)
# t=(1,[1,2])
# print(type(t), t)
# t[1][1]="test"
# print(t)

# l = ((i, j) for i in range(3) for j in range(3) if i!=j)
# print(l)
# print(tuple(l))

# N= 10
# l = [i**3 for i in range(N)]
# print(l.__sizeof__())
# l = (i**3 for i in range(N))
# print(l.__sizeof__())

# N= 10**3
# l = [i**3 for i in range(N)]
# print(l.__sizeof__())
# l = (i**3 for i in range(N))
# print(l.__sizeof__())

# N= 10**6
# l = [i**3 for i in range(N)]
# print(l.__sizeof__())
# l = (i**3 for i in range(N))
# print(l.__sizeof__())

#set 

# s = set()
# print(type(s), s)
# s = set("cbdsvbskdbvjkdbvjkfdbndmsbdvjfdsbfdj")
# print(type(s), s)
# s = {}
# print(type(s), s)
# s = {1,1,1,1,1}
# print(type(s), s)
# print([method for method in dir(set) if not method.startswith("_")])
# s = set("cbdsvbskdbvjkdbvjkfdbndmsbdvjfdsbfdj")

# print("c" in s)
# print("a" in s)
# print("aA" in s)
# s.add("AA")
# print(s)
# # s.add([1,2])
# t = s.pop()
# print(t, s)


# # dict
# d = dict()
# print(type(d), d)
# d = dict([[1,2], (3,4)])
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     "key1": 10,
#     12: 20,
#     55: "text"
# }
# print(type(d), d)
# # d[[1,1]] = 20
# d[(1,1)] = 99
# print(type(d), d)
# # t = (1,2, [11])
# # d[t] = 99
# print(type(d), d)

# d["key1"] = "text"
# d["key_1"] = "text"
# # print(d["key_2"])#error
# print(d.get("key_2"))#error
# print(d.get("key_2", "NoN Obj"))#error
# print([method for method in dir(dict) if not method.startswith("_")])

# print(d.fromkeys("abcd", 100))
# print(d.pop("key1"))
# print(d.popitem())
# print(d)
# d.update({121: 20, 55: 'Artur', (1, 2): 999})
# print(d)
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# for key, value in d.items():
#     print(key, value)

    
# for key in d:
#     print(key, d[key])


# class A:
#     def __init__(self, x=0, y=0) -> None:
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"{self.x=} {self.y=}"
#     def __lt__(self, other):
#         print("X")
#         return self.x > other.x 
#     def __add__(self, other):
#         return self.x > other.x
# p1 = A()
# p2 = A(1,2)

# print(p1, p2)
# print(p1> p2)