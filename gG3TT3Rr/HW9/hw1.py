import random

counter = 0

user_name = input ("Hi! What's your name? \n")
  
number = random.randint(1,100)

while counter<10:
    guess_number = int(input("Guess the number from 1 to 100, you only have 10 guesses! \n"))
    if guess_number == number:
      print(f"well done, {user_name}, you win!")
      break
    elif counter >= 9:
      print(f"Luck has turned against you today, {user_name} \nThe correct number was: ", number )
      break
    elif 1<= guess_number <=100 and guess_number < number:
      print(f"{user_name}, try bigger one")
      counter +=1
    elif 1<= guess_number <=100 and guess_number > number:
      print(f"{user_name} try smaller one")
      counter +=1
    elif not 1<= guess_number <=100:
      print(f"{user_name} this number not in range")
      counter +=1
