class Polygon:
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    
    def square(self):
        a, b = self.sides
        s = a * b
        print(f"Square of {a} and {b} is ", s)


t = Rectangle()
t.inputSides()
t.square()
