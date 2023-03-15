# Write a function that returns the largest number of two numbers
# (use DocString documentation strings in function_)

def comparison(a,b):
    """
    This function return the largest number of two from the input
    or returns a message of their equality
    """
    if a == b:
        return "numbers are equal"
    elif a>b:
        return a
    else:
        return b