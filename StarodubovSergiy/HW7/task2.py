# Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main program depending on the user's choice)

PI = 3.14

def rectangle(a,b):
    rectangle_area = a*b
    return rectangle_area

def triangle(base,h):
    triangle_area = 0.5*base*h
    return triangle_area

def circle(r):
    circle_area = PI*r**2
    return circle_area

choice = int(input("""What area you need to be calculated?
                   1. Rectangle
                   2. Triangle
                   3. Circle
                   """))

while choice != 1 and choice != 2 and choice != 3:
    print("please choose 1, 2 or 3")
    choice = int(input("""What area you need to be calculated?
                   1. Rectangle
                   2. Triangle
                   3. Circle
                   """))
    
if choice == 1:
    a = int(input("Please enter the value for side A: "))
    b = int(input("Please enter the value for side B: "))
    print(f"The area for rectangle with side A={a} and side B={b}: ", rectangle(a,b))
elif choice == 2:
    base = int(input("Please enter the value for Base: "))
    h = int(input("Please enter the value for Height: "))
    print(f"The area for triangle with base={base} and height={h}: ", triangle(base,h))
else:
    r = int(input("Please enter the radius of circle: "))
    print(f"The area for circle with radius={r}:", circle(r))