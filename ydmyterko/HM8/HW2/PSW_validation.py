def psw_validation(password):
    import re
    result=False
    if re.search('[a-zA-Z]', password) != None:
        if re.search('[0-9]', password) != None:
            if re.search('[$#@]', password) != None:
                if len(password) >= 6 and len(password) <= 16:
                    result=False
                else:
                    print("Error: Password length should be from 6 to 16 chars")
            else: print("Error: Password should have [$#@] chars")
        else: print("Error: Password should have [0-9] chars")
    else: print("Error: Password should have [a-z / A-Z] chars")

    return result
              
print("Your password is valid: ", psw_validation('1234567@'))