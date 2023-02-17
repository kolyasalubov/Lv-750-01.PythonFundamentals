number = input("Enter 4 digits number:")
print("You entered :", number)
list_of_digits = [int(i) for i in str(number)]

# Get product of number digits
product = 1
for digit in list_of_digits:
    product = product * digit
print("Product of the digit is:", product)

# Get revers number
revers_number = ""
for digit in list_of_digits:
    revers_number = str(digit) + str(revers_number)
print("Reverse number is:", revers_number)

# Get sorted number
sorted_number=""
for digit in sorted(list_of_digits):
    sorted_number = str(sorted_number) + str(digit)
print("Sorted number is:", sorted_number)