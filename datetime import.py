from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today<date(today,year,self.dob.month,self.dob.day):
            age-=1
            return age

person1 = Person("Anil","ab palli",date(2005,1,12))
print("calculated age for each person")
print("*****************")
print("Person1:")
print("Name:",person1.name)
print("Country:",person1.country)
print("Date of birth:",person1.date_of_birth)
print("Age:",person1.calculate_age())
