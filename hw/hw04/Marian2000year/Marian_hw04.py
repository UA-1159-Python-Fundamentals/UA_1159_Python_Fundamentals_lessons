print("1. Celsium in Fahrenheit enter 'F'")
print("2. Fahrenheit in Celsium enter 'C'")

choice = input("Your choice: ")

match choice.casefold():
    case 'f':
        celsius = float(input("Enter the temperature in Celsius to convert: "))
        if celsius < -273.15:
            print("Error: Temperature below absolute zero (-273.15)")
        else:
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} C is equivalent to {round(fahrenheit, 2)} F")
    case 'c':
        fahrenheit = float(input("Enter the temperature in Fahrenheit to convert: "))
        if fahrenheit < -459.67:
            print("Error: Temperature below absolute zero (-459.67)")
        else:
            celsius = (5 * fahrenheit - 160)/9
            print(f"{fahrenheit} F is equivalent to {round(celsius, 2)} C")
    case _:
        print("You entered invalid command")
            