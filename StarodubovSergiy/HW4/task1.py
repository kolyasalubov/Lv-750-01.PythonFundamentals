number = int(input("Provide the number you want factorial from: "))
factorial = 1

if number < 0:
    print("There is no factorial for negative amounts")
elif number == 0:
    print ("Factorial of 0 = 1")
else:
    for x in range(1,number+1):
        factorial = factorial*x
    print(factorial)