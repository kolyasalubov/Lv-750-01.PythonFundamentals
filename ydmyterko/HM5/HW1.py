list_digits = [1, 2, 4, 9]
print(type(list_digits))

for i in range(len(list_digits)):
    print(i)
    print(type(list_digits[i]))
    list_digits[i]=float(list_digits[i])
    print(type(list_digits[i]))

print(list_digits)
