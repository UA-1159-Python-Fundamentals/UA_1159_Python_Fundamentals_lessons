from rectangle import rectan_area
from triangel import triang_area
from circle import circle_area
__all__ = [rectan_area, triang_area, circle_area]

a = int(input("Choice yuor area: 1 rectangle, 2 triangle, 3 circle "))
if a == 1:
    a = int(input("Enter height "))
    b = int(input("Enter width "))
    area = rectan_area(a, b)
    print("Rectangele area ", area)
if a == 2:
    a = int(input("Enter width "))
    h = int(input("Enter height "))
    area = triang_area(a, h)
    print("Triangel area ", area)
if a == 3:
    r = int(input("Enter radius "))
    area = circle_area(r)
    print("Circle area ", area)
