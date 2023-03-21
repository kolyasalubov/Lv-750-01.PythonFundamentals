# Create a program that models a zoo. The program should have a base class Animal 
# that stores the animal's name, species, and number of legs. The class should have a 
# method make_sound that returns a string indicating the sound the animal makes. 
# The make_sound method should be overriden in the subclasses to return a sound 
# specific to each type of animal.

# Then, create three subclasses of Animal: Mammal, Bird, and Reptile. Each of these 
# subclasses should inherit the name, species, and number of legs from the Animal class.

# For the Mammal class, add a method give_birth and return "Roar" for make_sound method.

# For the Bird class, add a method lay_eggs and return "Squawk" for make_sound method.

# For the Reptile class, add a method shed_skin and return "Hiss" for make_sound method.


class Animal:
     def __init__(self, name, species, number_of_legs):
        self.name = name
        self.species = species
        self.number_of_leg = number_of_legs
        
        
     def make_sound(self):
        return "All animal make the sound"
        
class Mammal(Animal):
    def give_birth(self):
        return "Can give a birth"
    
    def make_sound(self):
        return "Roar"
    
class Bird(Animal):
    def lay_eggs(self):
        return (f"The birds are laying eggs")
    
    def make_sound(self):
        return "Squawk"
    
class Reptile(Animal):
    def shed_skins(self):
        return (f"The reptiles are shedding skin")
    
    def make_sound(self):
        return "Hiss"

