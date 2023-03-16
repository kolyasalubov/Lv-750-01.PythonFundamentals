class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
        
    def getInfo(self):
        return self.info