from typing import Self
class Student:
    def __init__(Self,name,classes):
        Self.name = name,
        Self.classes=classes

    def welcom(self):
        print("welcom to my chennal",self.name)

    def get_classes(self):
        return self.classes
class1_student = Student("rakesh","last")
class1_student.welcom()
print(class1_student.get_classes())
