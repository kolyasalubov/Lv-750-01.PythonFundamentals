class Employee:
    counter = 0
    def __init__(self, name, salary):
       Employee.counter += 1
       self.name = name
       self.salary = salary
       return print(f"{Employee.counter}: {name}, {salary}")
    
    def __del__(self):
        Employee.counter -= 1

a = Employee("Svetlana", 26000)
print(Employee.__doc__)
print(Employee.__base__)
print(Employee.__module__)
print(Employee.__name__)
print(Employee.__dict__)
