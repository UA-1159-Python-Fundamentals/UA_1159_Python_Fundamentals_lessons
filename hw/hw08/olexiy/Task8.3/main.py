from area_calculator import triangle_area,rectangle_area,circle_area
def main():
    choice=int(input("Площу якої фінури ви хотіли б обчислити: \n 1.Трикутник \n 2.Прямокутник \n 3.Коло \n"))
    if choice==1:
       triangle_area(3,5)
    elif choice==2:
       rectangle_area(5,6)
    elif choice==3:
       circle_area(5)
    else:
        print("Невірно вказане число")
if __name__ == '__main__':
    main()