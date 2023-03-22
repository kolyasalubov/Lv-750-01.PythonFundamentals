class Polygon:
    def __init__(self, sides):  # Конструктор класу Polygon, який ініціалізує список сторін фігури
        self.sides = sides
    
    def perimeter(self):  # Метод, який обчислює і повертає периметр фігури
        return sum(self.sides)
    
    def area(self):  # Метод, який обчислює площу фігури, проте не реалізований і повертає None
        pass


class Rectangle(Polygon):
    def __init__(self, length, width):  # Конструктор класу Rectangle, який ініціалізує довжину та ширину прямокутника
        super().__init__([length, width, length, width])  # Викликаємо конструктор батьківського класу та ініціалізуємо сторони прямокутника
        self.length = length  # Зберігаємо довжину прямокутника у вигляді атрибуту
        self.width = width  # Зберігаємо ширину прямокутника у вигляді атрибуту
    
    def area(self):  # Метод, який обчислює площу прямокутника
        return self.length * self.width
    
    def square(self):  # Метод, який обчислює площу квадрата, який має такі ж сторони, як і прямокутник
        return self.length**2