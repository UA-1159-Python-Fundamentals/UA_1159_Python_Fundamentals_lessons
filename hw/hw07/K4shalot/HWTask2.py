def rectangle(lenght, height):
    return lenght * height

def triangle(a, b):
    return 0.5*a*b

def circus(radius):
    return 3.14 * radius**2

print("Choose ur option beenwen 1-3: ")
print("1.Rectange\n 2.Triangle \n 3.Circus")
choice = int(input())
if(choice == 1):
    lenght = int(input("Lenght: "))
    height = int(input("Height: "))
    print("Area of Rectange: ")
    print(rectangle(lenght,height))
elif(choice == 2):
    a = int(input("Lenght drop to base of the triangle: "))
    b = int(input("Height:"))
    print("Area of Triangle: ")
    print(rectangle(a,b))
elif(choice == 3):
    radius = int(input("Input radius of the circus: "))
    print("Area of the circus: ")
    print(circus(radius))
else:
    print("Wrong number!(choose between 1-3)")