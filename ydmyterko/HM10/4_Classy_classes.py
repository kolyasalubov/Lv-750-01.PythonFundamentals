# Task
# Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter which should return johns age is 34
# Reference: https://docs.python.org/3/tutorial/classes.html

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @property
#     def info(self):
#         return '{}s age is {}'.format(self.name, self.age)

class Person:
    def __init__(self,name,age):
        self.info=f"{name}s age is {age}"

names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
    person=Person(name,age)
    print(person)