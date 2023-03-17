def rectangle(a, b):
    return a*b
  
def triangle(a, h):
    return a*h/2
  
def circle(r):
    return 3.14*r**2

print("Give me a number for calculate area of figure\n"
"(1 for rectangle; 2 for triangle; 3 for circle)")

choice = int(input("Enter your number: "))

match choice:
  case 1:
    print(f"The area of a rectangle: {rectangle(15, 20)}")
  case 2:
    print(f"The area of a triangle: {triangle(5, 10)}")
  case 3:
    print(f"The area of a circle: {circle(3.5)}")
  case _:
    print("Try 1,2 or 3")
