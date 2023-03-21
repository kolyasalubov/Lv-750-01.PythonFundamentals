def Rectangle_area():
    """Calculate Rectangle area"""
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area = a*b
    print("Rectangle area is:",area)
    return area

def Triangle_area():
    """Calculate Triangle area"""
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area = 1/2*a*b
    print("Triangle area is:",area)
    return area

def Circle_area(r):
    """Calculate Circul area"""
    r = int(input("Enter radius r: "))
    area = 3.14*r**2
    print("Circle area is:",area)
    return area

object = int(input("""Please enter number object 
                  for which you want to calculate area 
                  (rectangle - "1", triangle - "2", circule - "3"): """))
print("You enter ", object)
if int(object)==1:
    Rectangle_area()
elif object==1:
    Triangle_area()
elif object==2:
    Circle_area()
else:
    print("You entered wrong number. Please try again")



def Rectangle_area():
    """Calculate Rectangle area"""
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area = a*b
    print("Rectangle area is:",area)
    return area

def Triangle_area():
    """Calculate Triangle area"""
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area = 1/2*a*b
    print("Triangle area is:",area)
    return area

def Circle_area(r):
    """Calculate Circul area"""
    r = int(input("Enter radius r: "))
    area = 3.14*r**2
    print("Circle area is:",area)
    return area

object = int(input("""Please enter number object 
                  for which you want to calculate area 
                  (rectangle - "1", triangle - "2", circule - "3"): """))
print("You enter ", object)
if int(object)==1:
    Rectangle_area()
elif object==1:
    Triangle_area()
elif object==2:
    Circle_area()
else:
    print("You entered wrong number. Please try again")