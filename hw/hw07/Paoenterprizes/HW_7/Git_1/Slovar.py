str = input("Введіть речення: ")

def calc(str):
    char_calc = {}
    for i in str:
        if i != " ":
            if i not in char_calc:
                char_calc[i] = 1
            else: char_calc[i] += 1
    return char_calc
print(calc(str))