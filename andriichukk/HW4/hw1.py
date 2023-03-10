num = int(input("Enter your number: \n"))

factorial = 1

if num < 0:
    print("Factorial doesn't exist for negative numbers")
elif num == 0 or num == 1:
    print("The factorial is 1")
else:
    for number in range(1, num + 1):
        factorial = factorial * number
    print("The factorial of", num, "is", factorial)