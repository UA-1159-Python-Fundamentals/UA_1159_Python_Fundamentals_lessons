num = int(input("Введіть число: "))
num_str = str(num)
#Task_1

sum = 0
while num > 0:
    p = num % 10
    sum += p
    num = num // 10
print(sum)

# Task_2

print(num_str[::-1])

# Task_3

num_str_list = list(num_str)
num_str_list.sort(reverse=True)

print(''.join(num_str_list))
