import math

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

choice=int(input(""" Выберите фигуру: 
1-Прямоугольник
2-Треугольник
3-Круг 
Введите номер фигуры, площадь которой нужно обчислить: """))

if choice == 1: 
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    area = rectangle_area(width, height)
    print(f"Площадь прямоугольника = {int(area)}" )  
elif choice == 2: 
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = triangle_area(base, height)
    print(f"Площадь треугольника = {int(area)}" )
elif choice == 3: 
    radius = float(input("Введите радиус: "))
    area = circle_area(radius)
    print(f"Площадь круга = {int(area)}" )
else:
    print("Некоректный выбор, прочитай, что написано сверху")  