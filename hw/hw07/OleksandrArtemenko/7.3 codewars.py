import math
from functools import reduce


# Task1(https://www.codewars.com/kata/55225023e1be1ec8bc000390)
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# Task2(https://www.codewars.com/kata/simple-find-the-distance-between-two-points)
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


# Task3(https://www.codewars.com/kata/no-yelling)
def filter_words(st):
    arr = st.split(" ")
    res = []
    for word in arr:
        if word == "":
            continue
        res.append(word.strip().lower())
    return " ".join(res).capitalize()


# Task4(https://www.codewars.com/kata/convert-a-number-to-a-string)
def number_to_string(num):
    return str(num)


# Task5(https://www.codewars.com/kata/reversing-words-in-a-string)
def reverse(st):
    return " ".join(st.split()[::-1])


# Task6(https://www.codewars.com/kata/reverse-list-order)
def reverse_list(l):
    return l[::-1]


# Task7(https://www.codewars.com/kata/multiples-of-3-or-5)
def solution(number):
    if number < 0:
        return 0
    multiples = []
    for num in range(1, number):
        if num % 3 == 0:
            multiples.append(num)
        elif num % 5 == 0 and num not in multiples:
            multiples.append(num)

    return reduce(lambda x, y: x + y, multiples) if len(multiples) > 0 else 0


# Task8(https://www.codewars.com/kata/will-you-make-it)
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump - mpg * fuel_left <= 0


# Task9(https://www.codewars.com/kata/are-you-playing-banjo)
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.startswith("r") or name.startswith("R") else f"{name} does not play banjo"


# Task10(https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no)
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Task11(https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python)
def count_sheeps(sheep):
    return sheep.count(True)


# Task12(https://www.codewars.com/kata/is-this-my-tail/train/python)
def correct_tail(body, tail):
    return body[-1] == tail
