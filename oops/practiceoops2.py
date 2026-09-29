# Create a Car class with:

# brand
# model
# price

# Create 2 objects:

# Car 1

# brand = "BMW"
# model = "M4"
# price = 8000000

# Car 2

# brand = "Audi"
# model = "A6"
# price = 7000000

# Then print the brand and model of both cars.

# 💡 Hint: You already know everything required f


class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

car1=Car("BMW","M4",800000)
car2=Car("AUDI","A6",7000000)
print(car1.brand)
print(car2.brand)