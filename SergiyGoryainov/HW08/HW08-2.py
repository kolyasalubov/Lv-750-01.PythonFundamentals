# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

password = input("Enter a password: ")

if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,16}$', password):
    print("Password is valid.")
else:
    print("Password is invalid.")