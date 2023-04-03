def check_age(age):
  if age < 0:
    raise ValueError("Obtain error: number of your age can't be less than 0")

try:
    age = int(input("Enter your age: "))  
    check_age(age)

except ValueError as e:
   print(e)

else:
   if age %2 == 0:
    print("Your age is even")
   elif age %3 == 0:
    print("Your age is odd")
   else:
    print("Your age is odd")
