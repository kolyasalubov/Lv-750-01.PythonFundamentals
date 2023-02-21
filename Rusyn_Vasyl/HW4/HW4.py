input_number = int(input('Input some number?'))
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * (number-1)
print('Your input number is {}, and the factorial of number {} is {}'.format(input_number, input_number, factorial(input_number)))