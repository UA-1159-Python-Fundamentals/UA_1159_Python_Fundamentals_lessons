# def f():
#     "doc string for function f()"
#     a = 120
#     print(a)
# f()
# f()
# f()
# f()
# print(f())
# result = f()
# print(f"{result=}")
# # print(a)

# help(print)
# help(f)
# print(print.__doc__)
# print(f.__doc__)
# print(sum.__doc__)


# print(type(f))

# def greet(name):
#     """This function greets to the person"""
#     output= "Hello, " + name + ". Good morning!!!"
#     return output

# print(greet("Liubomyr"))
# print(greet("Andrii"))
# print(greet("Olha"))

# def my_func(number):
#     if number >10:
#         return "good"
#     print("end")

# print(my_func(5))
# print(my_func(55))


# name = "Andrii"


# def print_user(name):
#     name = "Max"
#     return name


# new_name = print_user("Oleh")
# print(f"{new_name=}")
# print(f"{name=}")


# def distance(x1, y1, x2, y2):
#     dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     print(dis)
#     return dis


# from random import randint


# def random_point(min, max):
#     print(randint(min, max), randint(min, max))
#     return randint(min, max), randint(min, max)


# points = []
# for i in range(5):
#     points.append(random_point(-10, 15))



# for i in range(len(points)-1):
#     dist = distance(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
#     print(f"[{points[i][0]}, {points[i][1]}] => {dist} => [{points[i+1][0]}, {points[i+1][1]}]")


# def my_f(a, b):
#     print(a, b)

# # my_f() #TypeError: my_f() missing 2 required positional arguments: 'a' and 'b'
# # my_f(15) #TypeError: my_f() missing 1 required positional argument: 'b'
# my_f(55, 99)
# # my_f(55, 99, 999) #TypeError: my_f() takes 2 positional arguments but 3 were given


# def my_f(a, b=10):
#     print(a, b)

# # my_f() #TypeError: my_f() missing 1 required positional argument: 'a'
# my_f(1)
# my_f(1, 22)
# # my_f(1, 22, 333) #TypeError: my_f() takes from 1 to 2 positional arguments but 3 were given


# def my_f(a, b=10, cc="text"):
#     print(f"{a=}\t{b=}\t{cc=}")
#     # print(f"a={a}\t{b}\t{c}")

#     print(a, b, cc)

# my_f(1,2,3)
# my_f(2,3,1)
# my_f(b = 2,cc=3,a=1)
# my_f(1,2,cc=33)
# my_f(a=1, 2, cc=33) # SyntaxError: positional argument follows keyword argument

# def my_f(a, b, c=1, d="t"):
#     pass
# def my_f(a, b=1, c, d="t"): pass # SyntaxError: parameter without a default follows parameter with a default


# def my_f(a, b, *args, c=1, d=2, **kwargs):
#     print(f"{a=}\t{b=}\t{args=}\t{c=}\t{d=}\t{kwargs=}\t")

# my_f(1,2,3,4,5,6,7,8, d="test", f=22, g=13)

# def my_f(a, b, c=1, d=2, **kwargs):
#     print(f"{a=}\t{b=}\t{c=}\t{d=}\t{kwargs=}\t")

# my_f(1,2,3,4,5,6,7,8, d="test", f=22, g=13) # TypeError: my_f() got multiple values for argument 'd'
# my_f(1,2,3,4,5,6,7,8, f=22, g=13) #TypeError: my_f() takes from 2 to 4 positional arguments but 8 were given
    

# def my_f(a, b, c=1, d=2, *args, **kwargs):
#     print(f"{a=}\t{b=}\t{args=}\t{c=}\t{d=}\t{kwargs=}\t")
# # my_f(1,2,3,4,5,6,7,8, d="test", f=22, g=13) # TypeError: my_f() got multiple values for argument 'd'
# my_f(1,2,3,4,5,6,7,8, f=22, g=13) # TypeError: my_f() got multiple values for argument 'd'

# def my_f( *args, **kwargs):
#     print(args, kwargs)

# my_f(1,2,3,4,5,6,7,8, f=22, g=13)
    
    

# def my_f(a, b, *args, c=1, d=2, **kwargs):
#     print(f"{a=}\t{b=}\t{args=}\t{c=}\t{d=}\t{kwargs=}\t")
# data = (1,2,3)
# data_key = {
#     "c": "CCC",
#     "d": "DDD",
#     "g": "GGG",
# }

# my_f(data[0], data[1], data[2], c=data_key["c"], d=data_key["d"], g=data_key["g"])
# my_f(*data, **data_key)
# my_f(*data, *data_key)
    
# def scope_func():
#     x = 10
#     print("Value inside function:", x)

# x = 20
# scope_func()
# print("Value outside function:", x)


# x=999

# def my_func_2():
#     print(x)

# my_func_2()


# x = 20
# def my_func():
#     print(x)
#     x = 30
#     print(x)
    

# my_func()

# def f(a):
#     if a>10:
#         return
#     return a**a

# print(f(5))
# print(f(55))

# l = []
# x = 20
# def my_func():
#     global x
#     l.append(10)
#     print(x)
#     x = 30
#     # l = 15
#     print(x)

# my_func()
# print(x)
# print(l)

# x = "global"
# def f():
#     x = "nonlocal"
#     print("f_s:", x)
#     def f2():
#         nonlocal x
#         x += "f2" 
#         print("f2:", x)
#     f2()
#     print("f_e:", x)

# f()
# print(x)


# def div(denominator):
#     deno = denominator
#     def inner_div(nominator):
#         return nominator/denominator
#     return inner_div

# div_5 = div(5)
# div_7 = div(8)

# print(div_5(15))
# print(div_5(33))
# print(div_5(-72))

# print(div_7(15))
# print(div_7(33))
# print(div_7(-72))



# def div(denominator):
#     deno = denominator**2
#     return deno

# def inner_div(nominator, denominator=div(3)):
#         return nominator/denominator
# print(inner_div(9))
# print(inner_div(9, 3))



# def rec(in_param):
#     print(in_param)
#     rec(in_param+1)

# import sys
# # sys.setrecursionlimit(3000)
# rec(0)

# def rec(in_param, indent=0):
#     print("\t"*indent, f"call rec({in_param})")
#     if in_param<5:
#         print("\t"*indent, in_param)
#         rec(in_param + 1, indent+1)
#         print("\t"*indent, in_param)
#     print("\t"*indent, f"end call rec({in_param})")
# rec(1)


# def div(a,b):
#     return a/b
# print(div(10, 20))

# div = lambda a, b: a/b**55

# print(div(10, 20))
# print(div(10, 20))
# print(div(10, 20))
# print(div(10, 20))




def s(element):
    if type(element) is list:
        return sum(element)
    else:
        return element


d1 = [22, 33]
d2 = [-99, 100]

l = [1, 2, 3, d1, d2 ]
# l.sort(key=s)
print(l)

l.sort(key=lambda element: sum(element) if type(element) is list else element)
key=(lambda element: sum(element)if type(element) is list else element, 1)
print(l)
# print(xxx)
print(key)
