# help(sum)
# print(sum.__doc__)

# def my_sum(a):
#     """
#     mydoc 
#     a: int
#     return: None
#     """
#     pass

# help(my_sum)
# print(my_sum.__doc__)

# import math

# from math import pi as PI, sin, cos as _cos
# print(dir())

# from math import *
# print(dir())

# t = math
# print(math.pi)
# print(math.sin)
# print(t.pi)
# print(t.sin(PI))
# print(PI)

# import sys,  os
# from pprint import pprint
# sys.path.append("c:\\data\\github\\UA_1159_Python_Fundamentals_lessons\\lessons\\lesson07")
# pprint(sys.path, indent=2)
# from lesson07 import s

# print(s(1))
# print(s([1,2,3]))


# print("<"*10)
# from func.fibo import fib, fib2
# print(">"*10)
# from func.fibo import fib, fib2
# from func import fibo
# from func.inner.fuctorial import fuctorial


# fib(5)

# print(fib2(5))
# print(fuctorial(5))

# print(__name__)

# if __name__ == "__main__":
#     print("run le.py")


# from func.inner.const import *
# print(dir())

# from func.inner.const import A, _A, __A
# print(dir())

from func.inner.const import *
print(dir())
from func.inner.const import A, _A, __A, B
print(dir())
from func.inner import const
print(const.A)
print(const._A)
print(const.__A)
print(const.B)