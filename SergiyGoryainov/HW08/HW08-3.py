import geometry

print("Which figure's area do you want to calculate?")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
choice = int(input("Enter your choice (1/2/3): "))

match choice:
    case 1:
        a = float(input("Enter length of rectangle: "))
        b = float(input("Enter breadth of rectangle: "))
        area = geometry.rectangle_area(a, b)
        print(f"The area of the rectangle is: {area}")
    case 2:
        h = float(input("Enter height of triangle: "))
        a = float(input("Enter base length of triangle: "))
        area = geometry.triangle_area(h, a)
        print(f"The area of the triangle is: {area}")
    case 3:
        r = float(input("Enter radius of circle: "))
        area = geometry.circle_area(r)
        print(f"The area of the circle is: {area}")
    case _:
        print("Invalid choice")