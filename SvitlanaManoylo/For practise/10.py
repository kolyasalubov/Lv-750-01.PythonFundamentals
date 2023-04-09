# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#      print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError):
# #      print("Error Occurred and Handled")
# list_num = []
# for i in 'bla23bla1bla8bla2':
#     try:
#         num = int(i)
#         list_num.append(num)
#     except ValueError:
#         continue
# print(list_num)
PI = 3.14
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(radius):
        return float((PI * radius**2))
        
    def getPerimeter(radius):
        return float((2 * PI * radius))
    
circy = Circle(11)
circy.getArea()
circy.getPerimeter()