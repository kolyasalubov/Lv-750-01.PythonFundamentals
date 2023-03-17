def zero_fuel(distance_to_pump, mpg, fuel_left):
    """ Gas calculation """
    if mpg*fuel_left >= distance_to_pump:
        return True
    else:
        return False
    