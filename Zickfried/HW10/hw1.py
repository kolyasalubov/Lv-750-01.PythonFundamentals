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