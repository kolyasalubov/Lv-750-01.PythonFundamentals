input_number = int(input('Input some number?'))

if input_number == 0:
    print(1)
else:
    result = 1
    for item in range(1,input_number+1):
        result *= item
    print('Your input number is {}, and the factorial of number {} is {}'.format(input_number, input_number, result))
