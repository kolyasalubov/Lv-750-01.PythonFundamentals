my_count = 0
user_name = input("Enter your user_name:")
while my_count <= 10:
    if input("Enter your login:") != "First":
        print("Error: please try again")
        my_count += 1
    else:
        print(f"Hello {user_name}")
        break  
print("Maximum number of tries exceeded, maybe you forget your login?")          