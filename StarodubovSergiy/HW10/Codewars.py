# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

# ball1 = new Ball();
# ball2 = new Ball("super");

# ball1.ballType     //=> "regular"
# ball2.ballType     //=> "super"

class Ball(object):
    # your code goes here
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Create a class Ghost

# Ghost objects are instantiated without any arguments.

# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

# ghost = new Ghost();
# ghost.color //=> "white" or "yellow" or "purple" or "red"

import random
class Ghost(object):
    # your code goes here
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

# You have to do God's job. The creation method must return an array of length 2 containing objects
# (representing Adam and Eve). The first object in the array should be an instance of the class Man. 
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human. 
# Your job is to implement the Human, Man and Woman classes.

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method 
# to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter 
# which should return johns age is 34

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

    def get_info(self):
        return self.info
    

# Now that we have a Block let's move on to something slightly more complex: a Sphere.

import math

class Sphere:
    def __init__(self, radius: float, mass: float):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    
# Timmy's boss

import re

class InvalidClassName(Exception):
    pass

def class_name_changer(cls, new_name:str):
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise InvalidClassName("Class name must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name