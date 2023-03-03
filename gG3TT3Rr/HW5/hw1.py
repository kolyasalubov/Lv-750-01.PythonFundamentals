# #1
# int_list = (list(range(11)))

float_list = []
for num in int_list:
    float_list.append(float(num))

print("Int list:", int_list)
print("Float list:", float_list)

#2
n = int(input("Введите число n: "))
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, a+b
