def solution(number):
    if number <= 0:
        return 0
    num1 = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            num1 += i
    return num1