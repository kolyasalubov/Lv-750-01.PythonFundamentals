def solution(number):
    counter = 0
    number = number - 1
    while number > 0:
        if number % 3 == 0:
            counter = counter + number
            number = number - 1
        elif number % 5 == 0:
            counter = counter + number
            number = number - 1
        else:
            number = number - 1
    return counter