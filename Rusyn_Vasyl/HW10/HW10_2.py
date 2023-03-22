class Human:
    species = "Homosapiens" # class variable

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def get_message():
        return "Hello, humans!"

# a = Human('Vasii')
# a.welcome()
# print(a.get_message())