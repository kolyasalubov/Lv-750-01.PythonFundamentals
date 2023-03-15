digit = int(input())
factorial_digit = 1

for i in range(digit):
    factorial_digit = factorial_digit * digit
    digit = digit - 1

print(factorial_digit)
