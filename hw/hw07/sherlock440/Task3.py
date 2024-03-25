# Method 1
def calculate_num_of_chars(string):
    answer = {}

    for element in string.lower():  # .lower() is for fucking the register off
        qty = string.lower().count(element)
        answer[element] = qty

    return answer

print(calculate_num_of_chars("lollipop"))


# Method 2 — Lambda funcs and dict comprehension are still hard for me, but I managed to develop this skill
calc_num = lambda string: {element: string.lower().count(element) for element in string.lower()}
print(calc_num("HelLo"))