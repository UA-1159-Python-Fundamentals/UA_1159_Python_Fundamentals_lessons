# Task9
name=input("Enter your name: ")
new_name=name.lower()
for letter in new_name:
    if letter[0] =="r":
        print(f"{name} plays banjo")
        break
    else:
        print(f"{name} doesnt play banjo")
        break
# Task6
def reverse(lst):
    return list(reversed(lst))
lst=[3,9,4,5,8]
print(reverse(lst))

# Task5
def reverse_word(str):
    lst=str.split(" ")
    return list(reversed(lst))
str="Hello world!"
print(reverse_word(str))

# Task10
def boolean(bool):
    if bool:
        return "Yes"
    else:
        return "No"
print(boolean(0))

# Task8
def will_you_make_it(gallons_left,nearest_pump):
    if gallons_left*25>=nearest_pump:
        return True
    else:
        return False
print(will_you_make_it(2,50))

# Task3
def filter_words(text):
    text_lower = text.lower()
    text_split = text_lower.split()
    joined_text = ' '.join(text_split)
    result = joined_text.capitalize()
    return result
print(filter_words("WOW this is REALLY          amazing!"))

# Task4
def number_to_string(number):
    return str(number)
num=int(input("Input number which you eant to convert: "))
print(f"{num} ==> \"{number_to_string(num)}\"")

# Task1
def greeting(name):
    lower_name=name.lower()
    if lower_name =='johny':
        return "Hello,my dear!"
    else:
        return f"Hello,{name}"
print(greeting("Johny"))

# Task12
def correct_tail(body,tail):
    if body[-1] == tail:
        return True
    else:
        return False
print(correct_tail("кішка","а"))

# Task11
def counting_sheep(sheep_list):
    present_sheep=0
    for sheep in sheep_list:
        if sheep==True:
            present_sheep+=1
    return present_sheep
sheep_list=[False,True,True,False,False,True,False]
print(counting_sheep(sheep_list))

# Task 2
from math import sqrt
def distance_points(x1,y1,x2,y2):
    return sqrt(((x1-x2)**2)+((y1-y2)**2))
print(distance_points(3,4,6,8))

# Task7
def solution(number):
    if number < 0:
        return 0
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result
print(solution(10))