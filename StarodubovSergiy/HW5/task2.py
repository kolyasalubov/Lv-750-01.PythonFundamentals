# Print Fibonacci numbers up to the entered number n, using cycles
# (Sequence of Fibonacci numbers 0,1,1,2,3,5,8,13, etc.)

n = int(input("Provide the number: "))

fibonacci = []

previous_number = 0
next_number = 1

while previous_number <= n:
    fibonacci.append(previous_number)
    sum = previous_number + next_number
    previous_number = next_number
    next_number = sum

print(fibonacci)