# oop: it helps us to build real world software.
## Class: Blueprint for creating object.
## Object: Instance of a class.
## Attribute: properties of an object.
## Method: Behaviours of an object.

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        print(f"Hello {self.firstname} {self.lastname}")

## object
student1 = Student("Binaya", "Shrestha")
student2 = Student("Ram", "Sharma")
student3 = Student("Hari", "Shrestha")

student1.fullname()
student2.fullname()
student3.fullname()




        