import math
def rec():
    a = int(input("Введіть висоту прямокутника: "))
    b = int(input("Введіть ширину прямокутника: "))
    return a*b
def trian():
    h = int(input("Введіть висоту трикутника: "))
    a = int(input("Введіть сторону трикутника: "))
    return 0.5*h*a
def cir():
    r = int(input("Введіть радіус кола: "))
    return math.pi * math.pow(r,2)