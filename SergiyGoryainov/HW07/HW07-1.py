# # Write a function that returns the largest number of two.

def larger_num(a, b):
    """This is very powerful function return larger number of the two numbers given. Use it wisely!"""
    return print(f'The larger of the two numbers is: {a}') if a > b else print(f'The larger of the two numbers is: {b}')

help(larger_num)
print(larger_num.__doc__)
larger_num(-10, -2)
