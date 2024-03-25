def solution(number):
    sol = 0
    for el in range(number):
        if el % 3 == 0 or el % 5 == 0:
            sol += el
    return sol

