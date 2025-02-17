class Person:
    def __init__(self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender
       

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

lists =[]
total_person = int(input("Enter the total number of person: "))
for i in range(total_person):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    gender = input("Enter the gender: ")
    person = Person(name, age, gender)
    lists.append(person)

for person in lists:
    person.display()
       