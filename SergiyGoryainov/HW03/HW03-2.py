four_digit_int = list(input('Enter 4-digit whole number '))

digit1 = int(four_digit_int[0])
digit2 = int(four_digit_int[1])
digit3 = int(four_digit_int[2])
digit4 = int(four_digit_int[3])
product = digit1 * digit2 * digit3 * digit4

reversed_list = four_digit_int[::-1]
reversed_number = ''.join(reversed_list)
sorted_number = ''.join(sorted(four_digit_int))

print(f'Product of the digits in the number is: {product}')
print(f' Here is your number reversed: {reversed_number}')
print(f' Here is your in ascending order: {sorted_number}')
