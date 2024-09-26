""".Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle.

"""
class rectangle:
    def __init__(self,length,width) :
        self.length=length
        self.width=width
        pass
    def cal_area(self):
        area_length=self.length
        area_width=self.width
        area=area_length*area_width
        print("Rectangle area:" ,area,"sq units")
rectangle1=rectangle(2,3)
rectangle2=rectangle(10,30)
rectangle3=rectangle(5,29)

print("Rectangle 1(2*3):")
rectangle1.cal_area()
print("Rectangle 2(10*30):")
rectangle2.cal_area()
print("Rectangle3 (5*15):")
rectangle3.cal_area()