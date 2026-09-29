# Now let's test whether you really understand self.

# Create a Person class with:

# name
# age

# Create a method:

# introduce()

# When called, it should print:

# My name is Prakash and I am 24 years old.

# Create the object and call the method.

# Hint

# Inside the method, you need to access the object's data:

# self.name
# self.age

# Try it yourself. Don't look for the solution—write it from your understanding.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"my name is {self.name} and i am {self.age}year old.")


firstPerson = Person("prakash",24)
firstPerson.introduce()