n = int(input("Enter number: "))

fib1, fib2 = 0, 1

print(fib1, fib2, end = ' ')

while fib2 <= n:
    fib_next = fib1 + fib2
    if fib_next <= n:
        print(fib_next, end = ' ')
    fib1, fib2 = fib2, fib_next