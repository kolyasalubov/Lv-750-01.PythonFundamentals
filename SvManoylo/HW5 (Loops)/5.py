# # Task 1
list = (10, 20, 30 ,40, 50)
for item in list:
    print(float(item))


# #Task 2
i1 = 0
i2 = 1

while i2 > 0:
    fib = i1 + i2
    print(fib)
    i1, i2 = i2, fib
    if fib > 75:
        break
print("The End")

#Task3 - first variant
for i in range (100):
    if i %2 == 0:
        print(i)

# #Task3 - second variant
i = 0
while i < 100:
    print (i)
    i += 2

#Task 4
for i in range (100):
    if i %2 != 0:
        print (i)

for i in range (100):
    if i %2 == 0:
        continue
    print (i)

#Task 5
numbers = [36,48,65]
for i in numbers:
    if i%2 != 0:
        break
    print ("List adding odd number")