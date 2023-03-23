numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

divisible_2 = []
divisible_3 = []
notdivisible_2_3 = []

for i in numbers:
    if i % 2 == 0:
        divisible_2.append(i)
    elif i % 3 == 0:
        divisible_3.append(i)
    else:
        notdivisible_2_3.append(i)
    i = i + 1
print(f"Even numbers that are divisible by 2 {divisible_2}")
print(f"Odd numbers, which are divisible by 3 {divisible_3}")
print(f"Numbers that are not divisible by 2 and 3 {notdivisible_2_3}")
