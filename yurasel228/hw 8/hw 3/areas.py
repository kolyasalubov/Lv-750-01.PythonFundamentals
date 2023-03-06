import math

def rectangle_area(a, b):
    return a * b

def triangle_area(h, a):
    return 0.5 * h * a

def circle_area(r):
    return math.pi * math.pow(r, 2)

shape = input("Обчислити площу якої фігури (прямокутник, трикутник, коло): ")
if shape == "прямокутник":
    a = float(input("Введіть довжину прямокутника: "))
    b = float(input("Введіть ширину прямокутника: "))
    print("Площа прямокутника: ", rectangle_area(a, b))
elif shape == "трикутник":
    h = float(input("Введіть висоту трикутника: "))
    a = float(input("Введіть довжину основи трикутника: "))
    print("Площа трикутника: ", triangle_area(h, a))
elif shape == "коло":
    r = float(input("Введіть радіус кола: "))
    print("Площа кола: ", circle_area(r))
else:
    print("Неправильна фігура. Спробуйте ще раз.")