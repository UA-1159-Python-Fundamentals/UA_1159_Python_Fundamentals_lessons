def banjo_checking(name):
    if name.startswith('R') or name.startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

print(banjo_checking("Ricky"))
print(banjo_checking("robbert"))
print(banjo_checking("Sasha"))