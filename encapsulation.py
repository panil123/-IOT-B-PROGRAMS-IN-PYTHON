class Employee:
    def __init__(self,name,age):
         self.name = name
         self.age = age
class SubEmployee(Employee):
    def Show_age(self):
       print("Age:",self.age)
emp = SubEmployee("Anil",20)
print(emp.name)
emp.Show_age()
