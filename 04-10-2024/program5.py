"""Problem Statement: Design a class hierarchy for an employee management system with the following structure:

Employee: Base class with name and salary.
Developer: Inherits from Employee with an additional attribute programming_language.
Manager: Inherits from Employee with an additional attribute team_size.
Intern: Inherits from Developer and has an additional attribute internship_duration.
Implement a method to display the details of each employee.

"""
class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"name :{self.name}")
        print(f"salary :{self.salary}")
 
class Developer (Employee) :
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language =programming_language
    def display_details(self):
        super().display_details()
        print(f"programming_language :{self.programming_language}")
 
class Manager (Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size =team_size
    def display_details(self):
        super().display_details()
        print(f"team_size:{self.team_size}")
 
class Intern (Developer):
    def __init__(self, name, salary, programming_language,intership_duration):
        super().__init__(name, salary, programming_language)
        self.intership_duration = intership_duration
    def display_details(self):
        super().display_details()
        print(f"intership duration:{self.intership_duration} months")
 
employee = Employee("Naveem",65000)
developer=Developer("Soni",4000,"sap")
manager = Manager("praveen",500000,9)
intern=Intern("navya",20000,"python",6)
 
print("Employee details:")
employee.display_details()
print("Developer details:")
developer.display_details()
print("Manager details:")
manager.display_details()
print("Intern details:")
intern.display_details()
