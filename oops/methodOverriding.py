# class Animal():
#     def sound(self):
#         print("animal make a sound....")

# class Dog(Animal):
#     def sound(self):
#         print("dog is barking.. ")
#         super().sound()


# dog1 = Dog()
# dog1.sound()

class Vehicle:
    def start(self):
        print("vehicle starts")

class Car(Vehicle):
    def start(self):
        print("car starts with key")
        super().start()

car1 = Car()
car1.start()
