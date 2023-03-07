#Task 1
a = int(input("First number - ", ))
b = int(input("Second number - ", ))
def largest_number(a, b):
    input = a, b
    """DocString:
    type a (int)
    type b (int)"""
    if a > b:
        print (f"The largest number {a}")
    else:
        print (f"The largest number {b}")
    return input
result = largest_number(a, b)
print(result)

#Task 2
print("Area of triangle - 1")
print("Area of rectangle - 2")
print("Area of circle - 3")
area_num = int(input("Choose area ", ))
PI = 3.14

def calc_area(area_num):
        if area_num == 1:
            a = int(input("Add side of triangle - a ", ))
            b = int(input("Add side of triangle - b ", ))
            area_of_triangle = (a * b) / 2
            print ("Area of triangle - ", area_of_triangle)
        elif area_num == 2:
            a = int(input("Add side of rectangle - a ", ))
            b = int(input("Add side of rectangle - b ", ))
            area_of_rectangle = a * b
            print ("Area of rectangle- ", area_of_rectangle)
        elif area_num == 3:  
            r = int(input("Add radius - r ", )) 
            area_of_circle = PI * r**2
            print ("Area of circle - ", area_of_circle)
        else:
            print ("Please, cose any area`a number")
        return print ("The end")

x = calc_area(area_num)
print(x)


#Task 3
string = input("Add new string: ")
def lst (string):
    new_lst = enumerate(string)
    print (list (new_lst))
a = lst(string)