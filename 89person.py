class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

p1 = Person("Som Prakash Chaudhary", 25, "Male")   
p2 = Person("Nishan Poudel", 22, "Male")
p3 = Person("Shankarsn Khadka", 25, "male")
p4 = Person("Ramesh Sharma", 25, "Male")

lists = [p1, p2, p3, p4]
for person in lists:
    person.display()
   
