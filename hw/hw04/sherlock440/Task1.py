degrees = float(input("Enter the temperature in Celsius: "))

if degrees < -273.15:
    print("Error: Temperature is below absolute zero (-273.15°C)")
else:
    f_degress = degrees * 9/5 + 32
    print(f"{degrees}°C is equivalent to {f_degress}°F, you american spy")