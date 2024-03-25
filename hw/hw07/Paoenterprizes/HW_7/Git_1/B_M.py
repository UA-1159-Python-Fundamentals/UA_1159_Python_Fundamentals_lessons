a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
def larg(a,b):
    """This function returns the largest number of two"""
    if a<b:
        return b
    else: return a
print(larg(a,b))