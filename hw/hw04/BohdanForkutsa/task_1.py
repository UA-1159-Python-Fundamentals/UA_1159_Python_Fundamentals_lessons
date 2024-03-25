celsius = float(input("Скільки градусів на дворі? "))

if celsius < -273.15:
    print("Співчуваю тобі, бажаю тепла")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"На дворі {fahrenheit}F")

