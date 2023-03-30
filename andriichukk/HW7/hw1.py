def largest_number(num1, num2):
    """
    function that returns the largest number of two numbers
    """
    if num2 > num1:
       large_num = num2
    else:
        large_num = num1
    return large_num

print(largest_number(5, 3))