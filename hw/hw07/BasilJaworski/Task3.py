def char_counter(string):
    """The function for count the number of each character in the string"""

    control_string = ""
    res = dict()

    for i in string:
        if i not in control_string:
            new_element = {i:string.count(i)}
            res.update(new_element)
            control_string += i

    return(res)

user_string = input("Please write something: ")
print(char_counter(user_string))