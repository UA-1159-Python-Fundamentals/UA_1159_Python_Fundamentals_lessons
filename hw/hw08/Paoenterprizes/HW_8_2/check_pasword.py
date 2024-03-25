import string
pw = input("Write your pasword: ")
if len(pw) not in range(6, 17):
    print("Error")
elif not any([1 if i in string.ascii_uppercase else 0 for i in pw]):
    print("Error")
elif not any([1 if i in string.ascii_lowercase else 0 for i in pw]):
    print("Error")
elif not any([1 if i in string.digits else 0 for i in pw]):
    print("Error")
elif not any([1 if i in string.punctuation else 0 for i in pw]):
    print("Error")
