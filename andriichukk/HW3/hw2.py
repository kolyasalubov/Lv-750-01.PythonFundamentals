# A four-digit natural number is specified
number = int(input("Please enter a four-digit natural number \n"))

if number < 1000 or number > 9999:
   print ("Please enter a four-digit natural number:")
elif number >= 1000 or number <= 9999:
   print ("Thank you! Your number is", number)
  
# find the product of the digits of this number
  
digits = str(number)
print ("The product of the digits of this number is", int(digits[0]) * int(digits[1]) * int(digits[2]) * int(digits[3]))

# write the number in reverse order

print('Your number in reverse' ,digits[::-1])

# in ascending order, you need to sort the numbers included in the given number

digitslist = list(str(number))
digitslist.sort()
print("Your number sort in ascending order ", digitslist)