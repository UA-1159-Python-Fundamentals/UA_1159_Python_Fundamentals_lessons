div_by_two = []
odd_div_thr = []
not_div = []

for i in range(1, 11):
    if i%2 == 0:
        div_by_two.append(i)

    if (i%2 != 0) and (i%3 == 0):
        odd_div_thr.append(i)

    if (i%2 != 0) and (i%3 != 0):
        not_div.append(i)


print(f"Numbers that are divisible by two: \t{div_by_two}")
print(f"Odd numbers divisible by three: \t{odd_div_thr}")
print(f"Not divisible by two and three: \t{not_div}")