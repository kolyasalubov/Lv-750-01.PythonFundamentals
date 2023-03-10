import area

object = int(input("""Please enter number object 
                  for which you want to calculate area 
                  ("1" - rectangle - , "2" - triangle, "3" - circule): """))
print("You enter ", object)

if int(object)==1:
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area.rectangle_area(a,b)
elif object==1:
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    area.triangle_area(a,b)
elif object==2:
    r = int(input("Enter radius r: "))
    area.circle_area()
else:
    print("You entered wrong number. Please try again")