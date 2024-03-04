cels = float(input("Enter a temperature in Celsius: "))

abs_zero = -273.15

far = (cels * 9/5) + 32

if cels < abs_zero:
    print("Error: Temperature below absolute zero (-273.15 °C)")
else:
    print(f'{round(cels, 2)} °C is equivalent to {round(far, 2)} °F')
    