import random

print('______'*10)
print('Lets find the number?'.center(60))
print('______'*10)

computer_number = random.randint(0,100)
human_number = -1
count = 0

while computer_number != human_number and count < 10:
    human_number = int(input('Your number please...'))
    if computer_number > human_number:
        count += 1
        print(f'Your number is less than computer and its your {count}th try')
    elif computer_number < human_number:
        count += 1
        print(f'Your number is more than computer and its your {count}th try')

    elif computer_number == human_number:
        print(f'Congratulations .... number is {computer_number}')


