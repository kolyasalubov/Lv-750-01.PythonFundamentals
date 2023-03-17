def func_larger_number(num1,num2):
    """This function return bigger number"""
    if num1>num2:
        result=num1
    elif num2>num1:
        result=num2
    else:
        result=None
    return result

print(func_larger_number.__doc__)