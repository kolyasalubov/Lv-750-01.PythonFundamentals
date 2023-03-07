def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance = mpg * fuel_left
    if distance >= distance_to_pump:
        return True
    else:
        return False
