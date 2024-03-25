#Task 1
#
#
#def comparison_larger_num(num1, num2):
#    """The function takes two numbers and returns the greater of them"""
#    if num1 <= num2:
#        return num2
#    elif num2 < num1:
#        return num1
# Test for task 1
#print(comparison_larger_num(1, 4))
#print(comparison_larger_num(1.5, 1.3))
#print(comparison_larger_num(-1, -2))
#print(comparison_larger_num(0, 0))


#Task 2
#
#
#def triangle_area(side_one, side_two, side_three):
#    """The function takes the sides of a triangle like number and returns its area (float)."""
#    p = (float(side_one) + float(side_two) + float(side_three)) / 2
#    return round((p * (p - float(side_one)) * (p - float(side_two)) * (p - float(side_three))) ** 0.5, 2)
#
#def rectangle_area(side_one, side_two):
#    """The function takes the sides of a rectangle like number and returns its area (float)."""
#    return round(float(side_one) * float(side_two), 2)
#
#def circle_area(r):
#    """he function takes radius of a circle like number and returns its area (float)."""
#    PI = 3.14159265358979
#    return round(PI * float(r) ** 2, 2)
#
#while True:
#    choose = input("The area of ​​which geometric figure do you want to get?\n 1. triangle\n 2. rectan\n 3. circle\n 4. exit\n - Your choose: ")
#
#    if choose not in "1234":
#        print("Error. You can choose only 1, 2, 3 or 4")
#
#    match choose:
#
#        case "1":
#            side_one = input("Enter the value of the first side\n - ")
#            side_two = input("Enter the value of the second side\n - ")
#            side_three = input("Enter the value of the third side\n - ")
#
#            print(f"Area of triangle = {triangle_area(side_one, side_two, side_three)}\n")
#
#        case "2":
#            side_one = input("Enter the value of the first side\n - ")
#            side_two = input("Enter the value of the second side\n - ")
#
#            print(f"Area of rectagle = {rectangle_area(side_one, side_two)}\n")
#
#        case "3":
#            r = input("Enter the radius of circle\n - ")
#
#            print(f"Area of circle = {circle_area(r)}\n")
#
#        case "4":
#            break


#Task 3
#
#
#def number_of_char(strng:str):
#    """A function that calculates the number of characters included in a given string""" 
#    count_dict = {}
#    for i in range(len(strng)):
#        if strng[i] in count_dict.keys():
#            count_dict[strng[i]] += 1
#        elif strng[i] not in count_dict.keys():
#            count_dict[strng[i]] = 1
#    return count_dict
#
#
#Test for task 3
#
#
#print(number_of_char("hellow"))
#print(number_of_char("HellowW"))
#print(number_of_char("          "))
#print(number_of_char(""))



    

