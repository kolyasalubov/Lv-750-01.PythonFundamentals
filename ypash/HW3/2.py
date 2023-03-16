digits = 1234

#  Task_1
a = digits // 1000
b = (digits % 1000) // 100
c = (digits % 100) // 10
d = digits % 10

print(a * b * c * d)


#  Task_2
print(d, c, b, a, sep="")


#  Task_3
sort_digits = (d, c, b, a)
print(sorted(sort_digits))

