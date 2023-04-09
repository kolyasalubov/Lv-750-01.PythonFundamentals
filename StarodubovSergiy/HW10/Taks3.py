# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee:
    """This is the Employee class."""
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    @classmethod
    def employee_count(cls):
        return cls.total_employees

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation string: {Employee.__doc__}")