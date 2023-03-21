import random

print ("Hello! It is the Guessed Game. You have 10 attemp to guess the number.")

guess_num = random.randint(1, 100)
attemp = 0

while attemp < 10:
    number = int(input("Please input any number from 1 to 100 -  ", ))
    if number == guess_num:
        print (f"Conratulation! You guess the number {guess_num}")
        break
    elif number > guess_num:
        print ("Your number is grether")
        attemp += 1
    else:
        print ("Your number is less")
        attemp += 1


if attemp == 0:
    print (f"Sorry. You already don`t have attemp! Try again. Tne number was - {guess_num}")