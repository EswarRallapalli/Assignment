"""Multilevel Inheritance
Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, 
and Manager is derived from Employee. 
Each class should add an additional attribute, and a method to display all attributes from the hierarchy.

Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information.
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee():
    def __init__(self,name,age,salary):
        Person. __init__(self,name,age)
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,age,salary,department):
        Employee.__init__(self,name,age,salary)
        self.department=department

    def display(self):
    
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Salary: {self.salary}")
        print(f"Department:{self.department}")
        
Manager=Manager("sunny",24,7000,"Analyist")
Manager.display()
    


