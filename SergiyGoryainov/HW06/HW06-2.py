# Checks the login entered by the user.
# If the login is "First", greet the user.
# If the login is different, send an error message.
# Use while loop.

login = ''
while login != 'First':
    print(f'Access denied. Please try again.', end='\n\n')
    login = str(input('Enter your login: '))
else:
    print(f'Welcome, {login}!')


# # One line longer
#
# while True:
#     login = input('Enter your login: ')
#     if login == 'First':
#         print(f'Welcome, {login}!')
#         break
#     else:
#         print('Access denied. Please try again.', end='\n\n')
