a=int(input("Give me an integer number for factorial: "))
factorial=1
for i in range (1,a+1):
  factorial*=i
  i += 1
print(factorial)