import abc
class Figure(abc.ABC):
    def area(self):
        pass
class Rectangle(Figure):
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2
    def area(self):
        return self.d1*self.d2
    def getDim(self):
        print("length=",self.d1)
        print("breadth=",self.d2)
r=Rectangle(2,5)
r.getDim();
print("Area of a rectangle=",r.area())
