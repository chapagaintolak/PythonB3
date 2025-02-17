class Customer:
    def __init__(self, acno, name, balance):
        self.acno = acno            
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= amount

    def display(self):
        print(f"account Number: {self.acno}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

customer1 = Customer(11, "Ramesh Sharma", 00)
customer2 = Customer(12, "Ram Sharma", 500)

customer1.deposit(1000)
customer1.withdraw(500)
customer1.deposit(100)

customer1.display()
customer2.display() 

