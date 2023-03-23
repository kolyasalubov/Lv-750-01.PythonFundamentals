import random

guess_number = random.randint(1, 10)
n=1
while n<10:
    user_number = int(input("Please guess a number:"))
    if user_number == guess_number:
        print("Congratulation! You guessed the number")
        break
    elif user_number < guess_number:
        print("The number is greater then this")
    elif user_number > guess_number:
        print("The number is less then this")
    else:
        print("Try again")
    n+=1

