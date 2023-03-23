import random

print("Вгадайте число від 1 до 100. У вас є 10 спроб.")

number = random.randint(1, 100)
guess_count = 0

while guess_count < 10:
    guess = int(input("Спроба № " + str(guess_count + 1) + ": "))
    guess_count += 1

    if guess < number:
        print("Загадане число більше.")
    elif guess > number:
        print("Загадане число менше.")
    else:
        print("Вітаємо! Ви вгадали число за " + str(guess_count) + " спроб.")
        break

if guess_count == 10:
    print("Ви вичерпали всі спроби. Загадане число було " + str(number) + ". Спробуйте ще раз.")