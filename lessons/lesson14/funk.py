def D(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        # return None
        raise Exception("d<0")
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b - d**0.5) / (2 * a), (-b + d**0.5) / (2 * a)


print(D(1, 2, -3))
