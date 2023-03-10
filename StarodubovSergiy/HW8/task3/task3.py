# Write a program that calculates the area of a rectangle S=a*b, the area of a triangle S=0.5*h*a,
# the area of a circle S=pi*r**2. This module must be used in another module in which we ask the user 
# the area of which figure he wants to calculate.
# (To perform the task, you need to import the math module, and from it the
#  pow() function and the value of the variable pi, and module, which contains three functions for 
#  finding areas, into the main program. The basic logic of the program is
#  executed in the main module)

import formulas

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
    print(f"The area for rectangle with side A={a} and side B={b}: ", formulas.rectangle(a,b))
elif choice == 2:
    base = int(input("Please enter the value for Base: "))
    h = int(input("Please enter the value for Height: "))
    print(f"The area for triangle with base={base} and height={h}: ", formulas.triangle(base,h))
else:
    r = int(input("Please enter the radius of circle: "))
    print(f"The area for circle with radius={r}:", formulas.circle(r))