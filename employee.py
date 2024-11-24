class Employee:
    company = "XYZ Corporation"
    location = "Nairobi"
    Employer = "Shah Noor"

    def __init__(self, name, age, year_joined, designation):
        self.name = name
        self.age = age
        self.year_joined = year_joined
        self.designation = designation

    def __str__(self) -> str:
        return f"{self.name} is the {self.designation} and joined the company in the year {self.year_joined}."
    
    def work(self, workPlace):
        return f"{self.name} works at the {workPlace}."
    
class Casual(Employee):

    def work(self, workPlace="factory"):
        return super().work(workPlace)
    
Employee1 = Employee("Emily akoth", 25, 2020, "Accountant")
Employee2 = Employee("John Kiriamiti", 32, 2019, "Manager")
print(Employee1)
print(Employee2)

Employee3 = Casual("Lydia Kemunto", 43, 2022, "laborer")
print(Employee3)
print(Employee3.work())