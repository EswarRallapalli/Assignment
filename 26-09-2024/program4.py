"""Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe"""
class Employee:
    bonus=0.1 
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def total_salary(self):
        return self.salary+(self.salary*Employee.bonus)   

emp1=Employee("sonia",120000)
emp2=Employee("ganesh",70000)
emp3=Employee("sunny",90000)

print("Initial Total Salaries:")
print(emp1.name,emp1.total_salary())
print(emp2.name,emp2.total_salary())
print(emp3.name,emp3.total_salary())
Employee.bonus=0.15

print("\nUpdate Total Salaries(15% bonus):")
print(emp1.name,emp1.total_salary())
print(emp2.name,emp2.total_salary())
print(emp3.name,emp3.total_salary())