class Human:
     def __init__(self, name):
        self.name = name
    
     def welcome(self):
        return f"Hello, {self.name}"

     @classmethod
     def classmethod(cls, species = "Homosapiens"):
        cls.species = species
        return cls.species

     @staticmethod
     def staticmethod():
        return 'arbitrary message called'

h1 = Human("John")

print(h1.welcome())
print(Human.welcome(h1))

print(h1.classmethod())
print(Human.classmethod())

print(h1.staticmethod())
print(Human.staticmethod())
