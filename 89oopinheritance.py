class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")



class Student(Person):
    def __init__(self, name, age, gender, roll_no):
        super().__init__(name, age, gender)
        self.roll_no = roll_no

    def display(self):
        super().display()
        print(f"Roll No: {self.roll_no}")

s1 = Student("Som Prakash", 25, "Male", 101)
s1.display()
