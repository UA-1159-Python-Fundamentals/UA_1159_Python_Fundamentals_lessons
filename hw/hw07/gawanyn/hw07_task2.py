def area_of_rectangle(length, width):
    """
    This function returns area of rectangle.
    """
    return length * width

def area_of_triangle(base, height):
    """
    This function returns area of triangle.
    """
    return base * height * 0.5

def area_of_circle(radius):
    """
    This function returns area of circle.
    """
    return 3.14*radius**2


print('1. Rectangle')
print('2. Triangle')
print('3. Circle')

choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
    area = area_of_rectangle(length, width)
    print("Area of rectangle is: ", area)
elif choice == 2:
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the width of height: "))
    area = area_of_triangle(base, height)
    print("Area of triangle is: ", area)
elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    area = area_of_circle(radius)
    print("Area of radius is: ", area)
else:
    print("Invalid choice")
    
