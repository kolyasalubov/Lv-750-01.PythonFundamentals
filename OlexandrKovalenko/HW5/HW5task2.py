n = int(input("Give number of Fibonacci members: "))
a = 0
b = 1
sequence = []
new = 0
count=0
if n <= 0:
   print("Please enter a number > 0: ")
else:
  while count<n:
    new = a+b
    a = b
    b = new
    count += 1
    sequence.append(new)
print(sequence, sep=", ")
