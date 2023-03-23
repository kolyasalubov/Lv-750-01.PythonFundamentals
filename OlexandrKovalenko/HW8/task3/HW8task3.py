import formulas_for_square

print("Give me a number for calculate area of figure\n"
"(1 for rectangle; 2 for triangle; 3 for circle)")

choice = int(input("Enter your number: "))

match choice:
  case 1:
    num1 = float(input("input a: "))
    num2 = float(input("input b: "))
    print(f"The area of a rectangle: {formulas_for_square.rectangle(num1, num2)}")
  case 2:
    num3 = float(input("input a: "))
    num4 = float(input("input h: "))
    print(f"The area of a triangle: {formulas_for_square.triangle(num3, num4)}")
  case 3:
    num5 = float(input("input radius: "))
    print(f"The area of a circle: {formulas_for_square.circle(num5)}")
  case _:
    print("Try 1,2 or 3")