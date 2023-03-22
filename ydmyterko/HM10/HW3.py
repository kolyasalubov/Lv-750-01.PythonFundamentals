class Employee:
    """Employee class"""
    def __init__(self):
        self.employee = {}

    def addEmployee(self, name, salary):
        self.employee.update({name:salary})

    def totalEmployee(self):
        print("Total number of employee is:", len(self.employee))

    def showEmployee(self):
        for x,y in self.employee.items():
            print(x,y)

company = Employee()
company.addEmployee("Yuriy", "10")
company.addEmployee("Ivan", "15")
company.addEmployee("Taras", "20")
company.showEmployee()
company.totalEmployee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
