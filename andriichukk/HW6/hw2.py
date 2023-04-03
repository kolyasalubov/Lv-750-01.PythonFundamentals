registered_login = input("Enter your login for registration: \n")

print("Thank you! Now you can login in")

login = input("Enter your login: \n")

while login == registered_login:
    print("Welcome")
    break
else:
    print("Error")



#################

# registered_login = "First"

# login = input("Enter your login: \n")

# while login == registered_login:
#     print("Welcome")
#     break
# else:
#     print("Error")