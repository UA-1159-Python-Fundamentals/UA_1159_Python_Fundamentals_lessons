tem_cels = float(input("Enter the temperature in Celsius: "))
print(f"{tem_cels}°C is equivalent to {(tem_cels * (9 / 5) + 32 )}°F" if tem_cels >= -237.15 else \
      "Error: Temperature below absolute zero (-273.15°C)")