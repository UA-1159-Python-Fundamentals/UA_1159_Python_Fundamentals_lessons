try:
    age = int(input("Enter your age: "))
    if age%2==0:
        print("Your age is even")
    if age%2==1:
        print("Your age is odd")
    if age < 1:
        raise TypeError("Your age must be real")
except ValueError:
    print("Age must be an integer.")
