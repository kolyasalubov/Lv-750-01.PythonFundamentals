def more_in_two(number_1, number_2):
    return max(number_1, number_2)

first_number = input('Please input your first number?')
second_number = input('Please input your second number?')



if first_number.isdigit() and second_number.isdigit():
    print(more_in_two(first_number, second_number))
else:
    print('Something wrong')
