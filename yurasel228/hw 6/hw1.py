upper_limit = int(input("Enter the upper limit of the range: "))
even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []
    
upper_limit = int(input("Enter the upper limit of the range: "))
    
for i in range(1, upper_limit+1):
    if i % 2 == 0:
        even_divisible_by_2.append(i)
    elif i % 3 == 0:
        odd_divisible_by_3.append(i)
    else:
        not_divisible_by_2_or_3.append(i)

print(f"{even_divisible_by_2}{odd_divisible_by_3}{not_divisible_by_2_or_3}")
    