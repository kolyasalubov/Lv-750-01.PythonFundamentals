password = str(input("Input your password   "))
spec_sym_list = ("$", "@", "#")
def check_password(password):
    message = ()
    for i in password:
        if i.isupper():
            message = "Unvalid password"
            break
        elif i.islower():
            message = "Unvalid password"
            break
        elif i.isdigit():
            message = "Unvalid password"
            break
        elif i != "@" or i != "#" or i != "$":
            message = "Unvalid password"
            break
        elif len(str(password)) < 6:
            message = "Unvalid password"
            break
        elif len(str(password)) > 18:
            message = "Unvalid password"
            break
        else:
            message = "Valid password"
    return message

result = check_password(password)
print(result)