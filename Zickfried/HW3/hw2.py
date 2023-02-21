number = input("Enter 4 digits number:")

print(number)
list_of_numbers = [int(i) for i in str(number)]

#find product
product = 1
for digit in number:
    product *= int(digit)
print(product)

#revers order
reverse_a = int(str(number)[::-1])
print(reverse_a)

#ascending order,sorted the numbers included in the given number
sorted_digit_str = "".join(sorted(str(number)))
sorted_a = int(sorted_digit_str)

print(sorted_a)



