number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    for number in range(1, number+1):
        factorial *= number
    print("Factorial of", number, "is", factorial)

