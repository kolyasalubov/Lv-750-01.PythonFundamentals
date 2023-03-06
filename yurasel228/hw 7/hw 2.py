import math

def rectangle_area(length, width):
    """
    Функція для обчислення площі прямокутника.
    Приймає довжину та ширину прямокутника як аргументи.
    Повертає площу прямокутника.
    """
    return length * width

def triangle_area(base, height):
    """
    Функція для обчислення площі трикутника.
    Приймає основу та висоту трикутника як аргументи.
    Повертає площу трикутника.
    """
    return 0.5 * base * height

def circle_area(radius):
    """
    Функція для обчислення площі кола.
    Приймає радіус кола як аргумент.
    Повертає площу кола.
    """
    return math.pi * radius**2

# Основна програма
print("Обчислення площі фігур")
print("1. Прямокутник")
print("2. Трикутник")
print("3. Коло")

choice = int(input("Виберіть фігуру (1/2/3): "))

if choice == 1:
    length = float(input("Введіть довжину прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))
    area = rectangle_area(length, width)
    print("Площа прямокутника: %.2f" % area)
elif choice == 2:
    base = float(input("Введіть основу трикутника: "))
    height = float(input("Введіть висоту трикутника: "))
    area = triangle_area(base, height)
    print("Площа трикутника: %.2f" % area)
elif choice == 3:
    radius = float(input("Введіть радіус кола: "))
    area = circle_area(radius)
    print("Площа кола: %.2f" % area)
else:
    print("Невірний вибір.")