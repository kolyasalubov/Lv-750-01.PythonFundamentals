print ("Area of triangle - 1")
print ("Area of circle - 2")
print ("Area of rectangle - 3")
num = int(input("Choose any number of area"))
from function import *

if num == 1:
    print(function.area_of_triangle(num))
elif num == 2:
    print(function.area_of_circle(num))
elif num == 3:
    print(function.area_of_rectangle(num))
else:
    print("Unexpected number!")

