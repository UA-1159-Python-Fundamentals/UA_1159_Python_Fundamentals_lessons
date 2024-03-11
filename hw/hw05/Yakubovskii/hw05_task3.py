n = int(input("Write any number: "))

m = 1
f = 1
while m <= n:
    f *= m
    m += 1
print(f"Your factorial number is: {f}")