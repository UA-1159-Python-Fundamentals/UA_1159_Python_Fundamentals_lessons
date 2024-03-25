print(__name__)
import math
def triangle_area(base,height):
    base=int(input("Введіть довжину основи: "))
    height = int(input("Введіть висоту: "))
    return print("Площа вашого трикутника: ",(0.5*base*height))

def rectangle_area(lenght,width):
    lenght = int(input("Введіть довжину: "))
    width = int(input("Введіть ширину: "))
    return print("Площа вашого прямокутника: ",(lenght*width))
def circle_area(radius):
    radius = int(input("Введіть радіус: "))
    return print("Площа вашого кола: ",(math.pi*math.pow(radius,2)))