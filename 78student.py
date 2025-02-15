print("Student Management Software")
print("1. Add Student")
print("2. View Student")
choice = int(input("Enter your choice: "))
adding = True  # multiple students can be added

while adding:
    if choice == 1:
        print("Add Student")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        file = open("students.csv", "a")
        file.write(f"{name},{age},{address}\n")
        file.close()
    elif choice == 2:
        print("View Student")
        file = open("students.csv", "r")
        print(file.read())
        file.close()
    
    question = input("Do you want to continue? (y/n): ")
    if question.lower() == "n":
        adding = False
    else:
        choice = int(input("Enter your choice(1. Add Student, 2. View Student): "))


# View this code: https://raw.githubusercontent.com/technologychannel/PythonB3/refs/heads/master/78student.py
# Create Stock Management 
# Product Name, Price, Qty [Fields]
# Functions:
# 1. Add Product
# 2. View Product
