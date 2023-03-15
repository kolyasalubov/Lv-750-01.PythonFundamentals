from math import pi

def area_of_triangle():
    a = int(input("Input side a - "))
    h = int(input("Input side h - "))
    area = 0.5 * h * a
    return print(area)

def area_of_circle():
    r = int(input("Enter radius - "))
    area = (pi * r)**2
    return print(area)

def area_of_rectangle():
    a = int(input("Input side a - "))
    b = int(input("Input side b - "))
    area = a * b
    return print(area)