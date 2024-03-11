num = int(input("Please enter Your number: "))

d = 1

if num == 0:
    print("Factorial Your number: 1")
else:
    l = list(range(2, num+1, 1))
    for i in l:
        d *= i
    print(f"Factorial of numbers {num}! = {d}")
