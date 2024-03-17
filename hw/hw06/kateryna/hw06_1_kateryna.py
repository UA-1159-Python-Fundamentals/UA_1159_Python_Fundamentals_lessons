n = list(range(1,11))
even_numbers_2 = []
odd_numbers = []
not_divisible_2_3 = []
for element in n:
        if element % 2 == 0:
            even_numbers_2.append(element)
        elif element % 3 == 0:
            odd_numbers.append(element)
        else:
            not_divisible_2_3.append(element)

print(even_numbers_2, "is an even number divisible by 2")
print(odd_numbers, "is an odd number divisible by 3")
print(not_divisible_2_3, "is neither divisible by 2 nor by 3")
