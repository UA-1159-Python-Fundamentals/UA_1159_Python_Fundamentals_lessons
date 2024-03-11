def count_fuel(gallons, distance):
    possible_distance = gallons * 25

    if possible_distance >= distance:
        return True

    return False

print(count_fuel(2, 50))
print(count_fuel(3, 50))
print(count_fuel(1, 50))