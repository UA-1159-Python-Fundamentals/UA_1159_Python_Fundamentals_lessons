a = input("Enter first variable: ")
b = input("Enter second variable: ")

print(f"a = {a} \nb = {b}")

a, b = b, a

print(f"Now:\na = {a} \nb = {b}")