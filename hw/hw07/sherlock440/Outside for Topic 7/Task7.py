def func(number):
    if number <= 2:
        return 0

    temporary_list = list(range(1, number))

    result = 0
    for elem in temporary_list:
        if elem % 3 == 0 or elem % 5 == 0:
            result += elem

    return result

print(func(20))