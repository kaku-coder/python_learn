class Person():
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

    def method(self):
        print(f"Your name is {self.name} and Your age is {self.age}")
    def is_adult(self):
        if self.age>18:
            return True
        else:
            return False


Person1 = Person("prakash",20)
Person2 = Person("madhab",12)

Person1.method()
Person2.method()
print(Person1.is_adult())
print(Person2.is_adult())