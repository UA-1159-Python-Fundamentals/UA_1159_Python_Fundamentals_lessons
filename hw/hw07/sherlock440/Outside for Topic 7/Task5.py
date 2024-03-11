def vice_versa(my_string):
    listed = my_string.split()
    listed = [element.strip() for element in listed]
    new_string = ' '.join(listed[::-1])

    return new_string

print(vice_versa("Hi There."))