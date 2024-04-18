from calculate_area import (rectangle_area, traingle,circle)


choice = int(input("Виберіть фігуру: \n 1.Rectangle "
                   "\n 2.Traingle \n 3.Circle \n "))
if choice==1:
    a = float(input("Довжина квадрата: "))
    b = float(input("Висота квадрата: "))
    area = rectangle_area(a, b)
    print(f"Площа квадрата = {area}")
elif choice==2:
    a = float(input("Довжина основи трикутника: "))
    h = float(input("Висота трикутника: "))
    area2 = traingle(a, h)
    print(f"Площа трикутника = {area2}")
elif choice==3:
    r = float(input("Введіть радіус кола: "))
    area3 = circle(r)
    print(f"Площа кола = {area3}")
else:
    print("невірно введено значення, спробуйте ще раз")
