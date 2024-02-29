#Temperature Converter

temperature_in_celsius = float(input("Enter a temperature in Celsius: "))

if temperature_in_celsius < -275.15:
    print("Error: Temperature below absolute zero (-273.15)")
else:
    temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32
    print(f"{temperature_in_celsius} is equivalent to {temperature_in_fahrenheit}")

