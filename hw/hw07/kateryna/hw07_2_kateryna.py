# Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice)
#Task_2

def rectangle(lenght, height):
    return lenght * height

def traingle(a, b):
    return 0.5 * a * b

def circle(radius):
    PI = 3.14
    return PI * radius ** 2

def main():
    choice = int(input("Виберіть фігуру: \n 1.Rectangle \n 2.Traingle \n 3.Circle \n "))
    if choice==1:
        lenght = float(input("Довжина квадрата: "))
        height = float(input("Висота квадрата: "))
        print(f"Площа квадрата = {rectangle(lenght, height)}")
    elif choice==2:
        a = float(input("Довжина основи трикутника: "))
        b = float(input("Висота трикутника: "))
        print(f"Площа трикутника = {traingle(a, b)}")
    elif choice==3:
        radius = float(input("Введіть радіус кола: "))
        print(f"Площа кола = {circle(radius)}")
    else:
        print("невірно введено значення, спробуйте ще раз")

main()