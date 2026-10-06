
from asyncio import selector_events
from typing import Self
from abc import ABC, abstractmethod 
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.height*self.width

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
    
def printAera(Shape):
    print(f"the aeria of the shpae is {Shape.area()}")

circle1 = Circle(5)
rect1 = Rectangle(4, 6)
tri1 = Triangle(10, 5)

# priting all  
printAera(circle1)  
printAera(rect1) 
printAera(tri1)