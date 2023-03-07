def quantity_symbol(str_input):
    char_count = {}
    for char in str_input:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

start = input('Для початку натисніть "S"\n'
              'Для закінчення уведіть щось інше')

while start == 'S':
    str_input = input('Уведіть текст де потрібно підрахувати символи')
    print(quantity_symbol(str_input))


