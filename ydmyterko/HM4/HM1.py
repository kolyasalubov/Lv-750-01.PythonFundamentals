number = int(input('Please enter a number: '))
print(f'Your number is {number}. Calculating factorial...')

i=1
factorial=1
while i<=number:
    factorial *= i
    i+=1

print(f'Factorial for "{number}" is "{factorial}"')

