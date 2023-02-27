attempt=0
while attempt<10:
    user_name = input('Please enter login: ')
    if user_name == "First":
        print('Congrats ', user_name)
    else:
        print('Error, please try again')
    attempt+=1
    
