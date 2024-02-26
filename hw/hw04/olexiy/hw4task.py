celsium_degree=int(input("Enter the temperature in Celsius:"))
if celsium_degree > -273.15:
   farenheit_degree = (celsium_degree * 1.8) + 32
   print(f"{celsium_degree}C is equivalent to {farenheit_degree}F")
else:
   print("Temperature below absolute zero (-273.15°C)")
