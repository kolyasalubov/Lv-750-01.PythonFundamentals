my_list = list(range(1,11))
for i in my_list:
    if i % 2 == 0:
        print ("числа делящиеся на 2:", i)

print("-" *25)

my_list = list(range(1,11))
for i in my_list:
    if i % 3 == 0:
        print ("числа делящиеся на 3:", i)

print("-" *25)

my_list = list(range(1,11))
for i in my_list:
    if i % 2 != 0 and i % 3 !=0: 
        print ("числа не делящиеся на 2 и на 3:", i)
