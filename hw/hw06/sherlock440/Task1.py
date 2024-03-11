my_list = list(range(1, 11))

even_2_numbers = []
odd_3_numbers = []
not_divisible_numbers = []
for element in my_list:
    if element % 2 == 0:
        even_2_numbers.append(element)
    elif element % 3 == 0:  # we do not need to check if it's even element or not, because the checking was done above
        odd_3_numbers.append(element)
    else:
        not_divisible_numbers.append(element)

print(f"""
Even numbers "that are divisible by 2" (such a weird statement, because any even number is divisible by 2):
{even_2_numbers}

Odd numbers that are divisible by 3:
{odd_3_numbers}

Other boring numbers:
{not_divisible_numbers}
"""""
)