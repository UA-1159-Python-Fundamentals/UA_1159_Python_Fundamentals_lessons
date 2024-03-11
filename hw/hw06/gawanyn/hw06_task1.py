numbers = range(1, 11)

even_divisible_by_2 = [num for num in numbers if num % 2 == 0]

odd_divisible_by_3 = [num for num in numbers if num % 2 != 0 and num % 3 == 0]

not_divisible_by_2_and_3 = [num for num in numbers if num % 2 != 0 and num % 3 != 0]

print(even_divisible_by_2)
print(odd_divisible_by_3)
print(not_divisible_by_2_and_3)


