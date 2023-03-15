class Human:

    def __init__(self, name):
        self.name = name
        name = (input("Enter your name: "))
        return print ("You specience is Homosapiens")
    
    def welcome_message(name):
        return print(f"Hello, {name}!")

@staticmethod
def arbitrary_message():
    return print("You are awesome! )")

I = Human
I.welcome_message("A")


