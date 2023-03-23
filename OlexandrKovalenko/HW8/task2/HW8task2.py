import re

while True:

    pattern = input("Create a password: ")
    larg = len(pattern)

    a = len(re.findall("[a-z]", pattern))
    b = len(re.findall("[A-Z]", pattern))
    c = len(re.findall("[0-9]", pattern))
    d = len(re.findall("[@#$]", pattern))

    if larg<6 or larg>16:
       print("Invalid length of password")
       continue
    elif a<1:
       print("No any low letter in password")
       continue
    elif b<1:
       print("No any upper letter in password")
       continue
    elif c<1:
       print("No any number in password")
       continue
    elif d<1:
       print("No any special symbol in password")
       continue      
    else:
       print("Password is possible")
    break