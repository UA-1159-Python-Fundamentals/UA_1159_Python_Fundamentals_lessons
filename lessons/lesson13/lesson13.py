# doubled_odds = [n * 2 for n in range(10) if n % 2 == 1]
# print(doubled_odds)
# doubled_odds = []
# for n in range(10):
#     if n % 2 == 1:
#         doubled_odds.append(n*2)


# doubled_odds = [(i,j,k) for i in range(5) for j in range(i) for k in range(j, i)]
# print(doubled_odds)

# doubled_odds = []
# for i in range(5):
#     for j in range(i):
#         for k in range(j, i):
#             doubled_odds.append((i,j,k))
# print(doubled_odds)



# vec1 = [3, 10, 2, "None"]
# vec2 = [-20, 5, 1]
# z = zip(vec1, vec2)
# print(list(z))
# vec1 = [3, 10, 2, "None"]
# vec2 = [-20, 5, 1]
# z = zip(vec1, vec2, vec1)
# # print(list(z))
# print("d", dict(z))



# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# z = zip(vec1, vec2)
# print(list(z))
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# print(dot_mul)


# l = [1, 2,3,4,"5", 3, "text", "t"]
# "".isdigit

# # print(sum(map(int, l)))
# print(sum(map(lambda x: int(x) if str(x).isdigit() else -100, l)))

# print(list(filter(lambda x: str(x).isdigit(), l)))

# from functools import reduce
# def my_sum(a, b):
#     c = a+b
#     print(f"{a}+{b}={c}")
#     return c
# print(f"{reduce(my_sum, [1,2,3,4,5])=}")
# print(f"{reduce(my_sum, [1,2,3,4,5], -25)=}")


# l = [1,2,3,4,5]

# it = iter(l)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for i in range(3):
#     print(i)

# r = range(3)
# print(r)
# r = iter(r)
# print(r)

# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

# for i in range(3):
#     print(i)
#     if i == 1:
#         raise StopIteration()
    
# print("end")



# class MyRange:

#     def __init__(self, stop, start=None,  step=None):
#         if start is not None:
#             self.start = stop
#             self.stop = start
#         else:
#             self.start = 0
#             self.stop = stop
#         self.step = step
#     def __iter__(self):
#         self.curent = self.start
#         return self
#     def __next__(self):
#         if self.curent <= self.stop:
#             x = self.curent
#             self.curent += 1
#             return x
#         else:
#             raise StopIteration
        
# print(list(MyRange(10)))
# print(list(MyRange(3, 10)))
# print(list(MyRange(-5, 10, 3)))



# def generate(n):
#     print("Inside my generator")
#     yield 0
#     yield 1


# my = generate(10)
# print(my)
# print(next(my))
# print(next(my))
# print(next(my))


# def generate(n):
#     print("Inside my generator")
#     while n > 0 :
#         print(n, end=" => ")
#         n -= 1
#         print(n)
#         yield n
#         print("next:")



# my = generate(10)
# print("="*10)
# print(my)
# print("="*10)
# print(next(my))
# print("="*10)
# print(next(my))
# print("="*10)
# print(next(my))


# def generate():
#     print("step 1")
#     yield 1
#     print("step 2")
#     yield 2
#     print("step 3")
#     yield 
#     print("step 4")
#     yield 4
#     print("step 5")
#     yield 

# g = generate()
# print("="*10)
# print(next(g))
# print("="*10)
# print(next(g))
# print("="*10)
# print(next(g))
# print("="*10)
# print(next(g))
# print("="*10)
# print(next(g))
# print("="*10)
# print(next(g))
# print("="*10)


# l = [i for i in range(100)]
# print(l.__sizeof__(), l)
# t = (i for i in range(100))
# print(t.__sizeof__(), t )


# l = [i for i in range(10000)]
# print(l.__sizeof__(),)
# t = (i for i in range(10000))
# print(t.__sizeof__())


# def generate1():
#     return 1
# print(generate1)
# g = generate1()
# print(g)

# def generate2():
#     yield 1

# print(generate2)
# g = generate2()
# print(g)


# def generate2():
#     yield 1
#     return 2

# print(generate2)
# g = generate2()
# print(g)
# # print(g())
# print(g.__next__())
# a = g.__next__()
# print(a)


# def my_bed_decorator(fun):
#     print("*"*10)
#     fun()
#     print("*"*10)

# def f():
#     print("text")

# f()

# t = my_bed_decorator(f)



def RRR(fun):
    def wraper(*args, **qwargs):
        print("*"*10)
        result = fun(*args, **qwargs)
        print("*"*10)
        return result
    return wraper

@RRR
def f1():
    print("11111111")
    return 1

@RRR
def f2():
    print("22222222")


# f1 = decorator(f1)
# f2 = decorator(f2)
    

f = f1()
print(f)
f2()
f2()
f1()

@RRR
def f3(n, k):
    print(str(n)*k)

f3(5, 8)



# def generate(n):
#     print("Inside my generator")
#     while n > 0 :
#         print(n, end=" => ")
#         n -= 1
#         print(n)
#         yield n
#         print("next:")
# @generate
# def f3(n, k):
#     print(str(n)*k)


# def param_decorator(symbol, count=10):
#     def decorator(fun):
#         def wraper(*args, **qwargs):
#             print()
#             print(symbol*count)
#             result = fun(*args, **qwargs)
#             # print(args, qwargs.items())
#             print(f"{fun.__name__}( {", ".join(map(str, args))}, {", ".join(map(lambda i: f"{i[0]}={i[1]}" ,qwargs.items()))}) = {result}" )
#             print(symbol*count)
#             print()
#             return result
#         return wraper
#     return decorator

# @param_decorator("=", 3)
# def my_sum(a, b):
#     return a+b

# @param_decorator("A", 5)
# def my_div(a, b):
#     return a/b

# s = my_sum(5, 10)
# d = my_div(5, 10)
# print(s)
# print(d)
# d = my_div(5, b=10)


def r(max):
    c = 0
    while c< max:

        yield list(range(c, c+10 if c+10 < max else max))
        c += 10


for i in r(152):
    print(i)