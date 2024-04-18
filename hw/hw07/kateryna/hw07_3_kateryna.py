
# Write a function that calculates the number of characters included given string
def amound(str):
    a = dict()
    for letter in str:
        a[letter] =  str.count(letter)
    return a

str = input("write a word: ")
print(amound(str))


