def temperature_converter():
    ABSOLUTE_ZERO = -273.15
    user_input = float(input("Please, enter the temperature in Celsius: "))
    if user_input < ABSOLUTE_ZERO:
        print(f"Error. Temperature {user_input}°C is below absolute zero: {ABSOLUTE_ZERO}°C")
    else:
        print(f"{user_input}°C is equivalent to {round((user_input * 9 / 5) + 32, 2)}°F")


temperature_converter()
