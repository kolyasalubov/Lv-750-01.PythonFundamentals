class Employee:
    num_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.num_of_employees}")

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__module__,)
print(Employee.__doc__)