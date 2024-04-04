import math
def rectangle(a,b):
    c = a*b
    return c
def triangle(h,a):
    s = 0.5 * h * a
    return s
def circle(r):
    s = math.pi * pow(r, 2)
    return s

print("Choose one option to calculate area of 1.Rectangle 2.Triangle 3.Circle ")
choice = int(input())
if(choice == 1):
    a = int(input("Lenght: "))
    b = int(input("Width: "))
    print(rectangle(a,b))
elif(choice == 2):
    h = int(input("h: "))
    a = int(input("a: "))
    print(triangle(h,a))
elif(choice == 3):
    r = int(input("r: "))
    print(circle(r))
else:
    print("1-3")

