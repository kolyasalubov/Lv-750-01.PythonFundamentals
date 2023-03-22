import re

def validate_password(input_password):
    flag = True
    while flag:  
        if len(input_password)<6 or len(input_password)>16:
            break
        elif not re.search("[a-z]",input_password):
            break
        elif not re.search("[0-9]",input_password):
            break
        elif not re.search("[A-Z]",input_password):
            break
        elif not re.search("[$#@]",input_password):
            break
        # Returns a match where the string contains a white space character
        elif re.search("\s",input_password):  
            break
    else:
        return f"{input_password} is valid password"
        flag = False
        break
    
    if flag:
        return f"{input_password} is invalid password"