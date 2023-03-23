def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg >= 2 and fuel_left >= 2:
        return True
    else:
        return False