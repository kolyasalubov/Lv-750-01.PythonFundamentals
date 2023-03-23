print("Circle's area - 1")
print("Triangl's area - 2")
print("Rectandle's area - 3")
import calc_figure_area

user_number = int(input("Choose one of figures: "))

if user_number == 1:
    print(calc_figure_area.circle_area(int(input("Enter radius: "))))
elif user_number == 2:
    print(calc_figure_area.triangle_area(int(input("Enter base: ")), int(input("Enter high: ")))) 
elif user_number == 3:
    print(calc_figure_area.rectandle_area(int(input("Enter a side: ")), int(input("Enter b side: "))))    