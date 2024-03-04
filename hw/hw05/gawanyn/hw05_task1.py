import random

integer_list = [random.randint(-10, 10) for _ in range(random.randint(1, 10))]

float_list = [float(_) for _ in integer_list]

print(integer_list)
print(float_list)