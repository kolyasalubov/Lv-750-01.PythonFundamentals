#1
num = input("Введите четырехзначное число: ")
product = 1
for digit in num:
    product *= int(digit)
print("Произведение цифр числа", num, "равно", product)
#2
reversed_number = num[::-1]
print(f"Числа в обратном порядке: {reversed_number}")
#3
digits=[int(i) for i in str(num) ]
digits.sort() 
sorted_num = int(''.join(str(i) for i in digits))
print (f" Отсортированные в порядке возрастания: {sorted_num}")