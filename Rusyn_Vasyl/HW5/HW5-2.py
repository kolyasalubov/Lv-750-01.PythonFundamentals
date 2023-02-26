fibonacci_list = [0,1]
fibonacci_number = int(input('Please, input Fibonacci number?'))
if fibonacci_number <= 2:
    print(fibonacci_list)
else:
    # while fibonacci_list.count() <= fibonacci_number:
    for item in range (2,fibonacci_number):
        fibonacci_list.append(fibonacci_list[item -1] + fibonacci_list[item-2])

# Цикл для виведення елементів по 5 у рядок
for i in range(0, fibonacci_number+2, 5):
    row = fibonacci_list[i:i+5]  # отримуємо п'ять елементів для поточного рядка
    print("{:<5} {:<5} {:<5} {:<5} {:<5}".format(*row))  # форматуємо та виводимо рядок


