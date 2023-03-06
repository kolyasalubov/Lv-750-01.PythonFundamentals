import math
from areas import rectangle_area, triangle_area, circle_area

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