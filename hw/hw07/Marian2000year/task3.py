def number_of_characters(string):
    output = {}
    string = string.casefold()
    for letter in string:
        count = string.count(letter)
        output[letter] = count
    return output

print(number_of_characters("Hhelllllo"))
