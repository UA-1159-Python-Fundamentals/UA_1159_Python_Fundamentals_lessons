c = float(input("Enter temperature in Celsius: "))
if c < -273.15:
    print("Error: Temperature below absolute zero")
else: print(f"That's { (c * 9/5) + 32} degrees Fahrenheit")