class Human:
    def __init__(self, name):
        self.name=name
    
    def welcome(self):
        print(f"Welcome {self.name}")

    @classmethod
    def species(cls):
        print("This is Homosapiens")

    @staticmethod
    def likes():
        print("Python is the best")

person = Human(input("Please enter a name: "))
person.welcome()
person.species()
person.likes()
