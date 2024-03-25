from main import *

print("Enter 1 to calculate the area of a rectangle")
print("Enter 2 to calculate the area of a triangle")
print("Enter 3 to calculate the area of a circle")

choice = int(input("Enter your choice: "))

if choice == 1:
    width = float(input("Enter width of rectangle: "))
    length = float(input("Enter length of rectangle: "))
    area = area_of_rectangle(width, length)
    print(f"Area of rectangle is: {area}")
elif choice == 2:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = area_of_triangle(base, height)
    print(f"Area of triangle is: {area}")
elif choice == 3:
    radius = float(input("Enter radius of circle: "))
    area = area_of_circle(radius)
    print(f"Area of circle is: {area}")
else:
    print("Wrong choice. Please select 1, 2, or 3.")
