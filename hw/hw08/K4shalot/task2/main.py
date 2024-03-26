LowwerLetters = "abcdefghijklmnopqrstuvwxyz"
CapitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
Symbols = "$#@"

MinCount = 6
MaxCount = 16
password = ""

password = input("Password: ")
if (any(char in password for char in LowwerLetters) and
    any(char in password for char in CapitalLetters) and
    any(char in password for char in Numbers) and
    any(char in password for char in Symbols) and
    MinCount <= len(password) <= MaxCount):
    print("Done")
else:
    print("Must be one letter (a-z), (A-Z), one number (0-9) and one symbol ($#@) and lenght (6-16)")