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
class Frog(Animal):
    def make_sound(self):
        print("wooo")


def animal_sound(animal):
    animal.make_sound()

animal1 = Dog("Tommy")
animal2 = Cat("Kitty")
animal3 = Frog("kutta frog")
animal_sound(animal1)
animal_sound(animal2)
animal_sound(animal3)

