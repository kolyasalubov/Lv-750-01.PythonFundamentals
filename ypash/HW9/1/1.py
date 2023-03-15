from random import randint

random_numbers = randint(1, 100)
counter = 0


for i in range(random_numbers):
    number = int(input("Enter a number from 1 to 100 (you have 10 tries): "))
    if number == random_numbers:
        print("Congratulations! You guessed the given number!")
        break
    else:
        counter = counter + 1
        if counter == 10:
            print("You didn't guess. Don't be upset =)")
            break
        else:
            if number < random_numbers:
                print(f"Your number is less than guessed, enter the next number. You have {10 - counter} attempts left")
            elif number > random_numbers:
                print(f"Your number is more than guessed, enter the next number. You have {10 - counter} attempts left")
            

        

