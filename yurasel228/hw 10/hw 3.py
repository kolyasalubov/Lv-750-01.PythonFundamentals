class Employee:

    num_employees = 0  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1

    def display_info(self):
        print(f"{self.name} earns {self.salary} per year.")

    @classmethod
    def display_num_employees(cls):
        print(f"There are {cls.num_employees} employees in the company.")
print(Employee.__base__) 
print(Employee.__name__) 
print(Employee.__module__)  
print(Employee.__doc__)  