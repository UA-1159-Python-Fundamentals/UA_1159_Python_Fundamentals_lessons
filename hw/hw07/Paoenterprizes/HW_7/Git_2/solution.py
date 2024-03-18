def solution(number):
    if number < 0:
        return 0
    num = 0
    for i in range(1, number):
        if i %3 == 0 or i % 5 == 0:
            num = num + i
    return num
print(solution(16))