print("Give me a number the day of (1 is Monday, 2 is Tuesday, etc.)")

try:
    choice = int(input("Enter your number: "))

    match choice:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")

    if choice > 7:
        raise ValueError("Obtain error: not exist!")
    elif choice <= 0:
        raise ValueError("Obtain error: not exist!")    

except ValueError as e:
   print(e)
