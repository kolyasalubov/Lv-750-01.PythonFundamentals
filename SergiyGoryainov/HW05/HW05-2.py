# Print Fibonacci numbers up to the number entered by the user
fibonacci_sequence = [0, 1]
how_long_is_the_list = int(input('How long would you like your Fibonacci sequence to be? '))
if how_long_is_the_list <= 2:
    print('That is too short! Try again!')
else:
    for i in range(how_long_is_the_list-2):
        fibonacci_sequence.append(fibonacci_sequence[-1]+fibonacci_sequence[-2])
    print(fibonacci_sequence, end='\n\n')
    print('Here you go!')
