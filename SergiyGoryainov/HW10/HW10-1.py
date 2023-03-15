# # Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle.
#
class Polygon:
    """This is a polygon class"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Is a {self.__class__.name} from {self.__class__.science}'

    science = 'geometry'
    name = 'polygon'


class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__(self)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


rect = Rectangle(10, 5)

print(rect)
print(rect.area())
