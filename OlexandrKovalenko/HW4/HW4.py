a=int(input("Give me an integer number for factorial: "))
if a<0:
  print("Factorial of negative number not exist")
factorial=1
for i in range (1,a+1):
  factorial*=i
  i += 1
if a>=0:
  print(factorial)
