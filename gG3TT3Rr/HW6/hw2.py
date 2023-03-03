while True:
    login = input("Enter your login: ")
    if login == "First":
        print(f"Welcome,{login}!")
        break
    else:
        print("Error: Invalid login. Please try again.")
        break