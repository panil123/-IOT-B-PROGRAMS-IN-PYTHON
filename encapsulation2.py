class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

    def show_salary(self):
        print("Salary:",self._salary)

emp = Employee("Anil",70000)
print(emp.name)
emp.show_salary()
