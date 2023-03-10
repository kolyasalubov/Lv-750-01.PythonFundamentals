password = input("Enter a password: ")

if len(password) < 6 or len(password) > 16:
    print("Password length should be between 6 and 16 characters.")
else:
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    has_special = False
    for char in password:
        if char in "$#@":
            has_special = True
            break


    if has_lower and has_upper and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password should contain at least one lowercase letter, one uppercase letter, one digit, and one of the following special characters: $, #, @.")