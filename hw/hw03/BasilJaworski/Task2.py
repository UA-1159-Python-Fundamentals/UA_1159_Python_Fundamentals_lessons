digit = input("Please enter four numbers digit here: ")

#Part1
digit_product = 1

for i in digit:
    digit_product *= int(i)

print(digit_product)

#Part2
print(int(digit[::-1]))

#Part3
print(int("".join(sorted(digit))))




