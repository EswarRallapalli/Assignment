""".Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others.

"""
class company:
    total_employee=0
    def __init__(self,name,department):
        self.name=name
        self.department=department
        company.total_employee +=1

    def display(self):
        print("Name:-",self.name)
        print("Department:-",self.department)
    @classmethod
    def get_total_employee(cls):
         return cls.total_employee
employee1=company("Sonia","saas")
print("Total Empolyee:",company.get_total_employee())
employee2=company("sunny","Markrting")
print("Total Emplyee:",company.get_total_employee())
employee3=company("naveen","software trainee")
print("Total Emplyee:",company.get_total_employee())
employee1.total_employee=100
print("empolyee1 total employee:",employee1.total_employee)
print("employee total employee:",company.get_total_employee())
print("Empolyee Details: ")
employee1.display()
print()
employee2.display()
print()
employee3.display()