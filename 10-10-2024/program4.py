""".Create a base class Employee with attributes name and salary,
 and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.
"""
class Employee :
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        print(f"name:{self.name},Salary:{self.salary}")
    def get_salary(self):
        print(f"Salary:{self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,departmemt):
        super().__init__(name,salary)
        self.department=departmemt
    def get_details(self):
        print (f"name:{self.name},Salary: {self.salary},Department:{self.department}")
class Developer(Employee):

    def __init__(self,name,salary,programing_language):

        super().__init__(name,salary)
        self.programing_language=programing_language
manager=Manager("sunny",30000,"IT")
developer=Developer("naveen",9000,"python")
manager.get_details()
developer.get_details()