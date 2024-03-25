def fibonacci(n):
    a, b = 0, 1
    fib = []
    while b <= n ** 2:
        fib.append(a)
        a, b = b, a + b
    if n in fib:
        print("Is a Fibonacci number:", fib)
    else:
        print("Is not a Fibonacci number:", fib)

n = int(input("Enter the number: "))
fibonacci(n)