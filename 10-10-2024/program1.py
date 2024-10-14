"""1.Create a class Vehicle with attributes brand and year.
 The class should have a method get_info() that returns the brand and year of the vehicle. 
 Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.
"""
class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def get_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
class Car(Vehicle):
        def __init__(self,brand,year,number_of_doors):
            super().__init__(brand,year)
            self.number_of_doors=number_of_doors
        def get_info(self):
            print( f"Brand:{self.brand},year:{self.year},Number of doors:{self.number_of_doors}")
class Motocycle(Vehicle):
     def __init__(self,brand,year,has_sidecar):
          super().__init__(brand,year)
          self.has_sidecar=has_sidecar
     def get_info(self):
          sidecar_status="yes" if self.has_sidecar else "no"
          print( f"Brand :{self.brand} ,year :{self.year},Has Sidecar :{sidecar_status}")
car=Car("TATA",2024,4)
motocycle=Motocycle("Rolay Enfield",2024,True)
print(car.get_info())
print(motocycle.get_info())
