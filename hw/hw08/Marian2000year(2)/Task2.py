tester1 = "abcdefghijklmnopqrstuvwxyz"
tester2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tester3 = "0123456789"
tester4 = "$#@"
MIN = 6
MAX = 16
password = ""

while True:
    password = input("Please enter password: ")
    if (any(char in password for char in tester1) and
        any(char in password for char in tester2) and
        any(char in password for char in tester3) and
        any(char in password for char in tester4) and
        MIN <= len(password) <= MAX):
        print("Accepted")
        break
    else:
        print(f"""
Your password must contain: 
At least 1 letter between [a-z]
At least 1 letter between [A-Z]
At least 1 number between [0-9]
At least 1 character from [@#$]
MIN {MIN} characters
MAX {MAX} characters
        """)
