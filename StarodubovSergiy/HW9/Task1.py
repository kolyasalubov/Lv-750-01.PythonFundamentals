# Task 1. Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)

import pygame
import random
import string

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Guess the Number")

font = pygame.font.Font(None, 36)

white = (255, 255, 255)
black = (0, 0, 0)

number = random.randint(1, 100)
tries_remaining = 10
game_over = False
guess_text = ""
message = ""

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(guess_text)
                except ValueError:
                    message = font.render("Invalid input. Enter a number between 1 and 100.", True, black)
                    guess_text = ""
                    continue

                tries_remaining -= 1

                if guess == number:
                    message = font.render("Congratulations! You guessed the number!", True, black)
                    game_over = True
                elif tries_remaining == 0:
                    message = font.render("Sorry, you ran out of tries. The secret number was " + str(number), True, black)
                    game_over = True
                elif guess < number:
                    message = font.render("Try a higher number. You have " + str(tries_remaining) + " tries remaining", True, black)
                else:
                    message = font.render("Try a lower number. You have " + str(tries_remaining) + " tries remaining", True, black)

                guess_text = ""
            elif event.key == pygame.K_BACKSPACE:
                guess_text = guess_text[:-1]
            else:
                char = event.unicode
                if char in string.digits:
                    guess_text += char

    screen.fill(white)
    guess_label = font.render("Guess a number between 1 and 100:", True, black)
    screen.blit(guess_label, (10, 10))
    guess_input = font.render(guess_text, True, black)
    screen.blit(guess_input, (10, 50))
    tries_label = font.render("You have " + str(tries_remaining) + " tries remaining", True, black)
    screen.blit(tries_label, (10, 90))

    if message:
        message_rect = message.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(message, message_rect)

    pygame.display.update()

pygame.time.delay(5000)
pygame.quit()