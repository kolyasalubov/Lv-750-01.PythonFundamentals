
def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14159 * radius ** 2


print("Which shape would you like to calculate the area for?")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print("The area of the rectangle is:", area)
elif choice == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print("The area of the triangle is:", area)
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print("The area of the circle is:", area)
else:
    print("Invalid choice. Please enter a number between 1 and 3.")