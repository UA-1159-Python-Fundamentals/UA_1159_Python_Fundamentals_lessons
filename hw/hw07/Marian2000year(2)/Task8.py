def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= fuel_left*mpg:
        return True
    else:
        return False