# Write a Python program to check validity of a password (input from users).
# Validation:
# At least 1 letter between [a-z] and 1 letter between[A-Z]
# At least 1 number between [0-9]
# At least 1 character from [$#@]
# Minimum length 6 characters
# Maximum length 16 characters

import re

password = str(input(f"""Enter your password. It should contain small letter, 
capital letter, number, special symbol $, #, @ 
and must be between 6 and 16 characters: \n""" ))
if len(password) < 6 or len(password) > 16:
    print(f"Password could be only between 6 and 16 characters")
else:
    if not re.search("[a-z]", password):
        print("Password should contain small letters")
    elif not re.search("[A-Z]", password):
        print("Password should contain capital letters")
    elif not re.search("[0-9]", password):
        print("Password should contain number")
    elif not re.search("[$#@]", password):
        print("Password should contain special symbols like $,#,@")
    else:
        print("Password is valid")
    