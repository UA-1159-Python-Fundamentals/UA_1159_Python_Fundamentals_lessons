num = int(input("Please enter Your number: "))
fib = 0
l_fib = []

while fib < num:
    l_fib.append(fib)
    if fib == 0:
        fib += 1
    else:
        fib = fib + int(l_fib[-2])

print(l_fib)