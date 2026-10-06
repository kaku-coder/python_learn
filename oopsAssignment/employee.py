class Employee():
    def __init__(self,salary):
        self.__salary = salary

    def set_salary(self,amount):
        self.__salary=amount
    def get_salary(self):
        return self.__salary

# Create a subclass called Manager that inherits from Employee:
class Manager(Employee):
    def add_bonus(self,amout):
        bonus_salary =self.get_salary()+amout
        self.set_salary(bonus_salary)
        print(f"the salary is {self.get_salary()}")

emp = Employee(50000)
print("Employee salary:", emp.get_salary())
manager1 = Manager(55000)
print("Manager initial salary:", manager1.get_salary())

manager1.add_bonus(5000)

print("Manager updated salary:", manager1.get_salary())