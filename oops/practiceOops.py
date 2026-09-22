class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avarage(self):
        sum = 0
        for value in self.marks:
            sum+=value
        print(f"hi {self.name} your avg score is : {sum/3}")


s1=Student("prakash",[99,98,97])
s1.avarage()