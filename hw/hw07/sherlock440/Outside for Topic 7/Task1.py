def greeting(name):
    if name == 'Johnny':
        return f"Hello, Johnny. I have been waiting for your entering for the whole week. Do it!"
    return f"Hello, {name}. Log out and call Johnny!"

name = input("What a big boy is entering me today?\n==> ")

print(greeting(name))