123
number = input("Введіть число: ")


product = 1
for i in number:
    product *= int(i)

print("Добуток цифр числа:", product)


reverse_number = number[::-1]
print("Число у зворотньому порядку:", reverse_number)


sorted_number = ''.join(sorted(number))
print("Число зі відсортованими цифрами:", sorted_number)