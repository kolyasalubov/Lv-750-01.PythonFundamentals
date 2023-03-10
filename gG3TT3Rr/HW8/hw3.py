import area
figure = input("Выберите фигуру (прямоугольник, треугольник, круг): ")
if figure == "прямоугольник":
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))
    print(f"Площадь прямоугольника = {area.rectangle_area(a, b)}")
elif figure == "треугольник":
    a = float(input("Введите основание треугольника: "))
    h = float(input("Введите высоту треугольника: "))
    area = area.triangle_area(a, h)
    print("Площадь треугольника = ", area)
elif figure == "круг":
    r = float(input("Введите радиус круга: "))
    area = area.circle_area(r)
    print("Площадь круга = ", area)
else:
    print("Выбрана неверная фигура")