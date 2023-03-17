def char_count(given_string):
    """A function that calculates a number of characters in a given string"""
    return print({char: given_string.count(char) for char in set(given_string)})


char_count('avada kedavra')