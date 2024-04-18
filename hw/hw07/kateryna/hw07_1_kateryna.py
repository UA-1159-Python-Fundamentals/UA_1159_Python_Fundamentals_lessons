def greet(name):
    """This function greets to the person"""
    output= "Hello, " + name + ". Good morning!"
    return output
print(greet("Katya"))


def my_f(num):
    if num > 9:
        return "Good"
    print("end")
print(my_f(10))
print(my_f(5))


#Task_1
def largest_num(a, b):
    """function that returns the largest number of two
numbers """
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "equal numbers"
print(largest_num(3, 5))
