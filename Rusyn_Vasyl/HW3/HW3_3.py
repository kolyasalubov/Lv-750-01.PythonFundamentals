# First variant
a = input("Уведіть а")
b = input("Уведіть b")

a, b = b, a
print (a, b)
print ("_____-----_____"*10)

#  The second one
A = int(input("Уведіть число A"))
B = int(input("Уведіть число B"))

A = A^B
B = A^B
A = A^B

print(A, B)