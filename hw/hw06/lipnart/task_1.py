l = list(range(1, 11))

even_num = []
odd_num = []
other_num = []

for i in l:
    if i % 2 == 0:
        even_num.append(i)

for i in l:    
    if i % 3 == 0:
        odd_num.append(i)

for i in l:
    if i not in even_num and i not in odd_num:
        other_num.append(i)

print(f"Even numbers that are divisible by 2: {even_num}")
print(f"Even numbers that are divisible by 3: {odd_num}")
print(f"Numbers that are not divisible by 2 and 3: {other_num}")