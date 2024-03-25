def my_foo(istr):
    c ={}
    for char in t:
        if char in c:
            c[char] +=1
        else:
            c[char] = 1
    return c

t = input("Enter text ")
output = my_foo(t)
for char, count in output.items():
    print(f'"{char}": {count}', end = ",")