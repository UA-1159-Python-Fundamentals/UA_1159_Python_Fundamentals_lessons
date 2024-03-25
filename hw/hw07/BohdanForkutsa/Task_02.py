
def calculate_area_rectangle(length, width):
    '''Function return area rectangle.'''
    return length*width

# print(calculate_area_rectangle(10, 5))

def calculate_area_triangle(a, h):
    '''Function return area triangle.
    a = side of a triangle.
    h = height of the triangle.'''
    return (a*h)/2

# print(calculate_area_triangle(10, 5))

def calculate_area_circle(r):
    '''Function return area circle.
    r = circle radius'''
    return 3.14*r**2
# print(calculate_area_circle(2))

client = input("Why do you want to calculate the area? \n'rectangle' \n'triangle \n'circle'\n \n")

match client:
    case "rectangle":
        par = []
        par1 = int(input("Write a lenght. \n"))
        par2 = int(input("Write a width. \n"))
        par.append(par1)
        par.append(par2)
        print("Rectangle have ",calculate_area_rectangle(*par), " area.")
    case "triangle":
        par = []
        par1 = int(input("Write side of a triangle. \n"))
        par2 = int(input("Write a height of the triangle. \n"))
        par.append(par1)
        par.append(par2)
        print("Triangle have ",calculate_area_triangle(*par), " area.")
    case "circle":
        par = int(input("Write a circle radius. \n"))
        print("Circle have ", calculate_area_circle(par), "area.")
    case _:
        print("Error!!! \nPlease, input correct.")
