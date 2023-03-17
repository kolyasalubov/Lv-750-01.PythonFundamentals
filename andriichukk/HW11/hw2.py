week = {1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"}

number = int(input("Enter your number from 1 to 7: \n"))

def week_day(number):
    try:
        if number < 1 or number > 7:
            raise ValueError ("Your number is not in this range from 1 to 7")
        else:
            return week[number]
    except ValueError:
        return "Your number is not in this range from 1 to 7"
    
print(week_day(number))