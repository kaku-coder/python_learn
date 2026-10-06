class Animal:
    def __init__(self, name: str):
        self.name = name
        
    def make_sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animal1 = Dog("Tommy")
animal2 = Cat("Kitty")

animal1.make_sound()
animal2.make_sound()
