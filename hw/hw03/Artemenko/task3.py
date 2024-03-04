def interchange(val1, val2):
    val1, val2 = val2, val1
    return val1, val2


a = 5
b = 25
print(f"Initial values: {a}, {b}")
a, b = interchange(a, b)
print(f"Values after interchange: {a}, {b}")

