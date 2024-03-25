n = int(input("enter the number up to which you want to know the result of Fibonacci: "))
a = 0
b = 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b