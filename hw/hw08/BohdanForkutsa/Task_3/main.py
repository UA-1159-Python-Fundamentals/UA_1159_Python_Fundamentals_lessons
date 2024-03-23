from func.funcArea import *

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

