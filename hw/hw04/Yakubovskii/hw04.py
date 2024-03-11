C = float(input("Print a temperature in celsius:"))
F = (C * 9/5) + 32

if C < -273.15:
    print("Temperature below absolute zero (-273.15°C)")
else:
    print(f"This is converting in to Fahrenheit: {F}")