num = int(input("Please enter number from fibonacci list: "))

fibo = [0, 1]

for item in range(2, num):
    newitem = fibo[item - 1] + fibo[item - 2]
    fibo.append(newitem)
print(fibo)