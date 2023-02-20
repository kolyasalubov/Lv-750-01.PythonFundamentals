number = int(input("Введіть число: "))

factorial = 1
for i in range(1, number+1):
    factorial *= i

print("Факторіал з ", number, "це", factorial)