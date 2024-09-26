"""1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information.
"""
class person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def update_age(self,age_new):
       self.age=age_new

    def display(self):
         print(f"name:{self.name}, age:{self.age},  gender:{self.gender}")
         #print("NAME:-",self.name)
         #print("AGE:-",self.age)
         #print("GENDER:-",self.gender)
print("persons Details")

person1=person("eswar",23,"male")
person2=person("naveen",34,"male")
person3=person("sunny",24,"female")
person1.display()
person2.display()
person3.display()
print("Upadating age")


person2.update_age(26)
print("Age updated")

person2.display()





    