import math

def rectangle_area(a,b):
    """Calculate Rectangle area"""
    area = a*b
    print("Rectangle area is:", area)
    return area

def triangle_area(a,b):
    """Calculate Triangle area"""
    area = 0.5*a*b
    print("Triangle area is:", area)
    return area

def circle_area(r):
    """Calculate Circul area"""
    area = math.PI * pow(r)
    print("Circle area is:", area)
    return area