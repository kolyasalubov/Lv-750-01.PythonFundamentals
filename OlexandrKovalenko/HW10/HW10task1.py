class Polygon:
    
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        #Polygon.__init__(self, 2)
        super().__init__(2)
                
    def findAreaRect(self):
        a, b = self.sides
        area = a*b
        print(f"The area of the rectangle is {area}")

rect=Rectangle()
rect.inputSides()
rect.findAreaRect()
