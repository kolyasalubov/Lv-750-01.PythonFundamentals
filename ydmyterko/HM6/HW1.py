divisible_by_2 = []
divisible_by_3 = []
divisible_by_2_and_3 = []

for i in range(1,10):
    print(i)
    if i%2==0:
        divisible_by_2.append(i)
    elif i%3==0:
        divisible_by_3.append(i)
    else:
        divisible_by_2_and_3.append(i)

print('Divisible by 2: ', divisible_by_2)
print('Divisible by 3: ', divisible_by_3)
print('DIvisible by 2 and 3: ', divisible_by_2_and_3)