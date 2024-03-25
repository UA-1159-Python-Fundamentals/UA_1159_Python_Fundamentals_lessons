C = float(input("Enter the temperature in Celsius: "))
F = (C * 9/5) + 32
if C < -273.15:
    print("Error: Temperature below absolute zero (-273.15C)")
else:
    print(f"{C}C is equivalent to {F}F")
