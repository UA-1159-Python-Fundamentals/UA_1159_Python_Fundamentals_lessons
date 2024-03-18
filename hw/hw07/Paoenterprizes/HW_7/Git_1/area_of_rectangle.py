def main():
    print("Оберіть спосіб обчислення площі прямокутника:\n1\tЧерез дві сторони\n2\tЧерез діагональ\n3\tЧерез периметр")
    choos = input("Введіть варіат: ")
    match choos:
        case "1":
            a = float(input("Введіть висоту прямокутника: "))
            b = float(input("Введіть ширину прямокутника: "))
            def area_rec_s(a,b):
                return a*b
            print(f"Площа прямокутника = {area_rec_s(a,b)}")
        case "2":
            a = float(input("Введіть сторону прямокутника: "))
            d = float(input("Введіть діагональ прямокутника: "))
            def area_rec_d(a,d):
                return a*(d**2-a**2)**0.5
            print(f"Площа прямокутника = {area_rec_d(a,d)}")
        case "3":
            a = float(input("Введіть сторону прямокутника: "))
            p = float(input("Введіть периметр прямокутника: "))
            def area_rec_p(a,p):
                return (p * a - 2 * a ** 2) / 2
            print(f"Площа прямокутника = {area_rec_p(a,p)}")
        case _:
            print("Помилка!!! Такого варіанту не існує")
            main()
main()