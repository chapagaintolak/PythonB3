# Create Class Teacher with attributes (fistsname, lastname and method (fullname)

class Teacher:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self):
        print(f"{self.firstname} {self.lastname}")

Teacher1 = Teacher("Salikram", "Adhikari")
Teacher2 = Teacher("Hari", "Sharma")        


Teacher1.fullname()
Teacher2.fullname()