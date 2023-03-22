import random

number_to_guess = random.randint(1, 100)

max_attempts = 10

attempts_made = 0

print("You have 10 attempts to guess the number!")

while attempts_made < max_attempts:
    user_guess = int(input("Enter your number (between 1 and 100): "))

    attempts_made += 1

    if user_guess == number_to_guess:
        print("Congratulations, you guessed the number - {number_to_guess}!")
        break
    elif user_guess < number_to_guess:
        print("Your guess is less. Try again.")
    else:
        print("Your guess is greater. Try again.")

if attempts_made == max_attempts:
    print("Sorry, you ran out of attempts. The number was", number_to_guess)