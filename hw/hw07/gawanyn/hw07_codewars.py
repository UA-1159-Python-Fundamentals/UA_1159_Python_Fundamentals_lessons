#Codewars
#Task 1 Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
    
#Task 2 Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)

#Task 3 No yelling!
def filter_words(s):
    words = s.split()
    return ' '.join([word.capitalize() if i == 0 else word.lower() for i, word in enumerate(words)])

#Task 4 Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Task 5 Reversing Words in a String
def reverse(st):
    st.split()[::-1]
    return " ".join(st.split()[::-1])

#Task 6 Reverse List Order
def reverse_list(l):
    return l[::-1]

#Task 7 Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    else:
        sum = 0
        for i in range(1, number):
            if (i % 3 == 0) or (i % 5 == 0):
                sum += i
        return sum
    
#Task 8 Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#Task 9 Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
#Task 10 Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return 'Yes' 
    else:
        return 'No'
    
#Task 11 Counting sheep
def count_sheeps(sheep):

  return sheep.count(True)

#Task 12 Is this my tail?
def correct_tail(body: str, tail: str) -> bool:
    return body[-1] == tail