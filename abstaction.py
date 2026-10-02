
from abc import ABC

class Animal(ABC):
    # abstraction
    def sound(self):
        pass
    # abstraction 
    def movement(self):
        pass


class Dog(Animal):
    def hello(self):
        return "woof"
    

dog=Dog()
print(dog)