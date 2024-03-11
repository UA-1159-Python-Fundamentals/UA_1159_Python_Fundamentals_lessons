def convert_to_float(lst):
    if isinstance(lst, list):
        floats = []
        for elem in lst:
            if isinstance(elem, int):
                floats.append(float(elem))
            else:
                floats.append(elem)
        return floats
    else:
        print("Please, insert a list with ints")
        return []


print(convert_to_float([1, 2, 3]))
print(convert_to_float([1, "text", 3]))  # if an element in a list is not int, it is moved to the result without changes
