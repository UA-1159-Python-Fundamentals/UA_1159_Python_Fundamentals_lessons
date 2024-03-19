# I.
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# II.
import math


def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)


# III.
def filter_words(st):
    words = st.split()
    filtered = ' '.join(word.capitalize() if i == 0 else word.lower() for i, word in enumerate(words))
    return filtered


# IV.
def number_to_string(num):
    return str(num)


# V.
def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


print(reverse("Hello World"))
print(reverse("Hi There."))


# VI.
def reverse_list(l):
    return l[::-1]


# VII.
def solution(number):
    if number < 0:
        return 0

    multiples = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    return sum(multiples)


# VIII.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


# IX.
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# X.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


# XI.
def count_sheeps(sheep):
    count = 0
    for value in sheep:
        if value == True:
            count += 1
    return count


# XII.
def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False
