"""2.Problem Statement: Create a base class Vehicle with attributes brand and model.
 Then, create two derived classes Car and Bike, both inheriting from Vehicle, and adding their own attributes and methods.

Tasks:
Define a base class Vehicle with attributes brand and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Create another derived class Bike that inherits from Vehicle and adds an attribute type.
Implement methods to display the details of the vehicles.
Create instances of both Car and Bike and display their information.

"""
class Vehicle:
    
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
class Car(Vehicle):
    def __init__(self,brand,model,num_doors):
        super().__init__(brand,model)
        self.num_doors=num_doors
    def display_info(self):
        super().display_info()
        print(f"number of doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self,brand,model,type):
        super().__init__(brand,model)
        self.type=type
    def display_info(self):
        super().display_info()
        print(f"TYPE: {self.type}")
car=Car("Tata", "coralla",4 )
bike=Bike("dio","soocty", "Abs")
print("CAR Detail:")
car.display_info()
print("BIKE Details: ")
bike.display_info()