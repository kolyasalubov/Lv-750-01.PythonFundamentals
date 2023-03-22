class Polygon():
    pass

class Rectangle(Polygon):
    """
    Init rectangle and calculate square. 
    """
    def __init__(self, side_1 = 0, side_2 = 0):
        self.side_1 = side_1
        self.side_2 = side_2
        
    def getRect_square(self):
        return self.side_1 * self.side_2  
    
rect_sq = Rectangle(8, 6)

print(rect_sq.getRect_square())  

#####another method
# class Polygon():
#     """
#     It's Polygon class
#     """
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
    
#     def inputSides(self):
#         self.sides = [float(input(f"Enter side {str(i+1)}: "))
#                                         for i in range(self.n)]
            
    
#     def __str__(self):
#         return f"It's {self.name}"   
     
# class Rectangle(Polygon):
#     """
#     Init rectangle and calculate square. 
#     """
#     def __init__(self):
#         Polygon.__init__(self, 2)
        
#     def getRect_square(self):
#         a, b = self.sides
#         Square = a * b
#         print(f"Square of Rectangle: {Square}")
    
# rect_sq = Rectangle()

# rect_sq.inputSides() 

# rect_sq.getRect_square()     