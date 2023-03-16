factorial = 1
n = 5
if n < 0:
    print('The factorial is only defined for non-negative integers')
else:
    for i in range(1, n+1):
        factorial *= i
    print(factorial)
