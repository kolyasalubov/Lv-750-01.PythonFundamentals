fibonacci_list = [0,1]
fibonacci_number = int(input('Please, input Fibonacci number?'))
if fibonacci_number <= 2:
    print(fibonacci_list)
else:

    for item in range (2,fibonacci_number):
        fibonacci_list.append(fibonacci_list[item -1] + fibonacci_list[item-2])

# Loop 'for' for output 5-th number in a row
for i in range(0, fibonacci_number+2, 5):
    row = fibonacci_list[i:i+5]  # Take 5 number in a list
    print("{:<5} {:<5} {:<5} {:<5} {:<5}".format(*row))  # Take Format and output


