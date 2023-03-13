dream_range = int(input('Input your range?'))
numbers_list = list(range(0, dream_range+1))

rounded = dream_range // 3
even_numbers = []
odd_numbers = []
another_numbers = []

for number in numbers_list:
    if number % 2 != 0 and number % 3 != 0:
        another_numbers.append(number)
    elif number % 2 == 0 and number % 3 != 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print('Your start range is from 0 to {}\n'
      'even numbers is {}\n'
      'your odd numbers is {}\n'
      'another numbers is {}'.format(dream_range, even_numbers, odd_numbers, another_numbers))
