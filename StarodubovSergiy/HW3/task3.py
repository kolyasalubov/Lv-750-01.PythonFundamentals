# interchange the values of two variables without using the third variable
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
a,b = b,a
print("now they are switched :)")
print("Now, A = {} and B = {}".format(a, b))