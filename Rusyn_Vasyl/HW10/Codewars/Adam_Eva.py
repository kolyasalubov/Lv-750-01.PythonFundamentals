class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Man(Human):
    def __init__(self, name):
        super().__init__(name, "male")

class Woman(Human):
    def __init__(self, name):
        super().__init__(name, "female")

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]