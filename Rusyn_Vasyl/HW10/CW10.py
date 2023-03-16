class Car():
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    def start(self, status):
        return f'The {self.name} is {status} now'

    def stop(self, status):
        return f'The {self.name} is {status} now'


audi = Car('Audi', 'Carrr', 'S-class')
audi2 = Car('Audi', 'Carrr', 'b-class')
audi3 = Car('Audi', 'Carrr', 'c-class')
audi4 = Car('Audi', 'Carrr', 'a-class')

print(audi4.start('Mooving'))
print(audi2.start('Mooving'))
print(audi2.start('Mooving'))
print(audi3.start('Mooving'))