import math

def rectangle_area(a, b):
    return a * b

def triangle_area(h, a):
    return 0.5 * h * a

def circle_area(r):
    return math.pi * math.pow(r, 2)

shape = input("Which shape would you like to calculate the area for? (rectangle, triangle, circle): ")

if shape == "rectangle":
    a = float(input("Enter the length of one side: "))
    b = float(input("Enter the length of the other side: "))
    print("The area of the rectangle is:", rectangle_area(a, b))
elif shape == "triangle":
    h = float(input("Enter the height of the triangle: "))
    a = float(input("Enter the length of the base: "))
    print("The area of the triangle is:", triangle_area(h, a))
elif shape == "circle":
    r = float(input("Enter the radius of the circle: "))
    print("The area of the circle is:", circle_area(r))
else:
    print("Invalid input. Please enter rectangle, triangle, or circle.")