def foo_rectangle(a, b):
    rec1 = a * b 
    print("Area of ​​the rectangle: ", rec1)
def foo_triangle(a, b):
    tri1 = (a*1/2) * b
    print("Area of ​​the triangle: ", tri1)
def foo_circle(r):
    cir1 = 3.14 * r**2
    print("Circle radius: ", cir1)
selection = int(input("Enter number function rectangle '1', triangle '2', circle '3'"))
if selection == 1:
    a = int(input("Enter length one "))
    b = int(input("Enter length second "))
    foo_rectangle(a, b)
if selection == 2:
    a = int(input("Enter length one "))
    b = int(input("Enter length second "))
    foo_triangle(a, b)
if selection == 3:
    r = int(input("Enter radius "))
    foo_circle(r)
    


