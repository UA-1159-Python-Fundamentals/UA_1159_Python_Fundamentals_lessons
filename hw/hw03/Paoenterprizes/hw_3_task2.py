import math

numbers = input("Введіть число з четьрох чисел: ")
numbers = list(numbers)
product = 1
for i in numbers:
    product *= int(i)
print(product)

print(numbers[-1], numbers[-2], numbers[-3], numbers[-4], sep="")

print(sorted(numbers))