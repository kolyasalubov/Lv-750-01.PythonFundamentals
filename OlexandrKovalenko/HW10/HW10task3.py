class Employee:
    """
    An employee class. Each employee has characteristics such as name and salary. 
    The class have a counter that calculates the total number of employees, as well
    as a method that prints the total number of employees and a method that displays
    information about each employee in particular, namely the name and salary.
    """
    counter_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter_of_employees +=1

    @classmethod
    def counter(cls):
        return cls.counter_of_employees
    
    def display_data(self):
        return f"{self.name}: {self.salary}"
    
emp1 = Employee("John", 30000)
print(emp1.display_data())
emp2 = Employee("Linda", 30000)
print(emp2.display_data())
emp3 = Employee("Michael", 21000)
print(emp3.display_data())
emp4 = Employee("Tom", 15000)
print(emp4.display_data())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
