import random

int_list = [random.randint(1, 99999), random.randint(1, 99999), random.randint(1, 99999), random.randint(1, 99999), random.randint(1, 99999)]

float_list = []
for element in int_list:
    float_element = float(element)
    float_list.append(float_element)

print(int_list)
print(float_list)