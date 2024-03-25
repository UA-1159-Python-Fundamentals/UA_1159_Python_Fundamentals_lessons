def fibonacci(n):
    a = 0
    b = 1

    fibonacci_list = []

    while a <= n:
        fibonacci_list.append(a)
        if b <= n:
            fibonacci_list.append(b)
        a = a + b
        b = b + a

    for elem in fibonacci_list:
        print(elem, end=" ")
    print()

    if fibonacci_list[-1] < n:
        print(f"There is no exact value of {n} in fibonacci sequence, so sequence was made to {fibonacci_list[-1]}")


fibonacci(1597)
fibonacci(1598)
