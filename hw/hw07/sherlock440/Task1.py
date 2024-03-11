def find_the_max(a, b):
    """
    This super important and difficult function returns the biggest number of two given ones

    :param a: (int, float) — we both have no clue what will happen if you enter unsupported data type, so don't push your luck
    :param b: (int, float) — we both have no clue what will happen if you enter unsupported data type, so don't push your luck
    :return: (int, float)
    """
    if a > b:
        return a

    elif a < b:
        return b

    else:
        return

print(find_the_max(1,1))