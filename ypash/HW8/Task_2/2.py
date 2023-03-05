import re

password = input("Enter your password ",)

if len(
    re.findall("[a-z]", password)
    ) > 0 and len(
    re.findall("[A-Z]", password)
    ) > 0 and len(
    re.findall("\d", password)
    ) > 0 and len(
    re.findall("[$#@]", password)
    ) > 0 and len(password) <= 16 and len(password) >= 6:
    print("Valid")
else:
    print("Invalid")




