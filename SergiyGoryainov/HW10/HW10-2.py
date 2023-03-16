# Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homo Sapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name
        print(f'A {self.__class__.name} was born')

    name = 'Human'
    species = 'Homo Sapiens'

    def __str__(self):
        return f'{self.name} is a {self.__class__.name} from {self.species}'

    def greet(self):
        print(f'Hello human named {self.name}')

    @classmethod
    def info(cls):
        print(f'{cls.name} is {cls.species}')
    @staticmethod
    def msg():
        print(f'Here is the msg form static method')


sarah = Human('Sarah')

print(sarah)
sarah.greet()
sarah.info()
sarah.msg()