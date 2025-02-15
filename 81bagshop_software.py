import csv
from turtle import update
from prettytable import PrettyTable
def display_menu():
    print("\nWelcome to ABC Bagshop Software\n")
    
    menu_table = PrettyTable()
    menu_table.field_names = ["Option", "Description"]
    menu_table.align["Description"] = "l"  # Left align the descriptions

    # Add menu options
    menu_table.add_row(["1", "Add Product"])
    menu_table.add_row(["2", "List Product"])
    menu_table.add_row(["3", "Delete Product"])
    menu_table.add_row(["4", "Update Product"])
    menu_table.add_row(["5", "Search Product"])
    menu_table.add_row(["6", "Show Product by ID"])

    print(menu_table)  # Display the menu table
def list_product():
    print("List Product\n")
    # Create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names = ["ID", "Name", "Qty", "Price","Total"]
    table.align["Name"] = "l"
    with open("bag_shop_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for line in csv_reader:
            table.add_row([line[0], line[1], line[2], line[3],float(line[2])*float(line[3])])  # Add rows to the table
    
    print(table)  # Print table

### Search Product
def search_product(nameini):
    print("Search Product\n")
    # Create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names = ["ID", "Name", "Qty", "Price","Total"]
    table.align["Name"] = "l"
    with open('bag_shop_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[1][0].upper() == nameini[0].upper():
                table.add_row([line[0], line[1], line[2], line[3],float(line[2])*float(line[3])])
        print(table)
        print("Product not found.")

# Add Product
def add_product(id, name, qty, price):
    with open('bag_shop_data.csv','a',newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([id, name, qty, price])
        print("Product added successfully.")

# Show By ID
def show_by_id(id):
    print("Show Product\n")
    # Create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names = ["ID", "Name", "Qty", "Price","Total"]
    table.align["Name"] = "l"
    with open('bag_shop_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == id:
                table.add_row([line[0], line[1], line[2], line[3],float(line[2])*float(line[3])])
        print(table)

def update_product(id):
    print("Previous Record")
    show_by_id(id)
    print("Update Record")
    name = input("Enter New Name: ")
    qty = input("Enter New Quantity: ")
    price = input("Enter New Price: ")
    
    with open('bag_shop_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == id:
                row[1] = name
                row[2] = qty
                row[3] = price
                break
    with open('bag_shop_data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
        print("Product updated successfully.")

def delete_product(id):
    with open('bag_shop_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == id:
                rows.remove(row)
                break
    with open('bag_shop_data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
        print("Product deleted successfully.")

# Start Program
display_menu()
choice = int(input("Enter your choice: "))

if choice == 1:
    id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = input("Enter Product Quantity: ")
    price = input("Enter Product Price: ")
    add_product(id, name, qty, price)
elif choice == 2:
    list_product()
elif choice == 3:
    id = input("Enter Product ID: ")
    delete_product(id)
elif choice == 4:
    id = input("Enter Product ID: ")
    update_product(id) 
elif choice == 5:
    name = input("Enter Product Name: ")
    search_product(name)
elif choice == 6:
    id = input("Enter Product ID: ")
    show_by_id(id)
else:
    print("Invalid Choice")
    

# Create Visitor Entry System For Bank [Nabil Bank]
# ID, Date, Visitor Name, Purpose, 
# Add Following Option
# "1", "Add Visitor"
# "2", "List Visitor"
# "3", "Delete Visitor"
# "4", "Update Visitor"
# "5", "Search Visitor"
# "6", "Show Visitor by ID"
