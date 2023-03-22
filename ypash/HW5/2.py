fib_1 = 1
fib_2 = 1

n = int(input())

print(fib_1)
print(fib_2)

i = 2
while i < n:
    fib_sum = fib_2 + fib_1
    fib_1 = fib_2
    fib_2 = fib_sum
    i = i + 1
    print(fib_sum)