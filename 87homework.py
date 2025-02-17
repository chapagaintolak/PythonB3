## class Laptop with properties: id, name, ram and create 3 objects of it and print all detail
# Class house with properties: id, name, price]. cerate a constructor of it and create 3 objects of it. Add them to the list and print all detail.
# Create Class Teacher with attributes (fistsname, lastname and method (fullname)

class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name 
        self.ram = ram
    def display(self):
        print(f"{self.id} {self.name} {self.ram}")

Laptop1 = Laptop(1, "Dell", "8GB")        
Laptop2 = Laptop(2, "Asus", "16GB")        
Laptop3 = Laptop(3, "Lenovo", "16GB")

Laptop1.display()
Laptop2.display()       
Laptop3.display()     



class House:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def display(self):  
        print(f"{self.id} {self.name} {self.price}")

House1 = House(1, "Kathmandu", 50000)           
House2 = House(2, "Bhaktapur", 60000)
House3 = House(3, "Lalitpur", 70000)

House1.display()        
House2.display()
House3.display()