n = int(input("enter your number: "))

a = 1
factorial = 1
while a <= n:
    factorial *= a
    a += 1
print(factorial)