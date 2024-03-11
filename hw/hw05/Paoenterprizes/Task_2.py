n = float(input("inpun n: "))
fibo = 0
fibo_0 = 0
fibo_1 = 1
while fibo < n:
    fibo = fibo_0 + fibo_1
    if fibo > n:
        break
    fibo_0 = fibo_1
    fibo_1 = fibo
print(fibo)