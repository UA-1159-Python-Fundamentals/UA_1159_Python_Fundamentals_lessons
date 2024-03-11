n = int(input("n: "))

fibo_0 = 0
fibo_1 = 1

print(fibo_0)
print(fibo_1)

while True:
    fibo_next = fibo_0 + fibo_1
    if fibo_next > n:
        break
    print(fibo_next)
    fibo_0 = fibo_1
    fibo_1 = fibo_next
