age = int(input("Enter your age: \n"))

def enter_age(age):
    try:
        if age <= 0:
            raise ValueError("That is not a positive number!")
        elif age % 2 == 0:
            return f"Your age {age} is even!"
        else:
            return f"Your age {age} is odd!"
    except ValueError:
        return "That is not a positive number! Enter your age."

print(enter_age(age))