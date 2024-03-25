n = int(input("n: "))

i = 1
factor = 1

while i <= n:
    factor *= i
    i += 1
print(factor)