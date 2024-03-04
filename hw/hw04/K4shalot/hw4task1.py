print("Enter the temperature in Celsius: ")
celsium = int(input())

Fahrenheit = ((celsium *  (9 / 5)) + 32)
absolute_zero = -273.15

if (Fahrenheit < absolute_zero):
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    print("Fahrenheit temperature: {Fahrenheit}")