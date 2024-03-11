
# Task7.1
def comparison(a,b):
    """This program returns the largest number"""
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return print("Вони рівні")
print(comparison(7,9))


# Task7.2
def triangle_area(base,height):
    return 0.5*base*height
def rectangle_area(lenght,width):
    return lenght*width
def circle_area(radius):
    return 3.14*radius**2
def main():
    choice=int(input("Площу якої фінури ви хотіли б обчислити: \n 1.Трикутник \n 2.Прямокутник \n 3.Коло \n"))
    if choice==1:
        base=int(input("Введіть довжину основи трикутника: "))
        height = int(input("Введіть висоту опущену на основу трикутника: "))
        print("Площа вашого тикутника: ",triangle_area(base,height))
    elif choice==2:
        lenght = int(input("Введіть довжину прямомокутника: "))
        width = int(input("Введіть ширину прямокутника: "))
        print("Площа вашого прямокутника: ",rectangle_area(lenght,width))
    elif choice==3:
        radius = int(input("Введіть радіус вашого кола: "))
        print("Площа вашого кола: ",circle_area(radius))
    else:
        print("Невірно вказане число")

main()

# Task 7.3
def foo(str):
    d=dict()
    for letter in str:
        d[letter]=str.count(letter)
    return d
print(foo("hello"))

