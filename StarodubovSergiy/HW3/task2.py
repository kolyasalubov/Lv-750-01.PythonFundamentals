# part 2
number = list(input("input 4-digit number:"))
a = int(number[0])
b = int(number [1])
c = int(number [2])
d = int(number [3])
product = a*b*c*d
print("the product of digits is:",product)
print("number in reverse:", number[::-1])
number.sort()
print("number in ascending order:", number)