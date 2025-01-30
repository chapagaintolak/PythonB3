# Suppose You Are Building Software For Bag Shop.
# You have to add new product [id, name, qty, price]
# List the product
# Delete the product
# Update the product
# Search the product
import csv
from prettytable import PrettyTable
def display_menu():
    """Display the menu options in a PrettyTable format."""
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

    print(menu_table)  # Display the menu table
def list_product():
    print("List Product\n")
    
    # Create a PrettyTable instance
    table = PrettyTable()
    
    # Define the column names
    table.field_names = ["ID", "Name", "Qty", "Price"]
    table.align["Name"] = "l"
    with open("bag_shop_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for line in csv_reader:
            table.add_row([line[0], line[1], line[2], line[3]])  # Add rows to the table
    
    print(table)  # Print table

# Add Product
def add_product(id, name, qty, price):
    with open('bag_shop_data.csv','a',newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([id, name, qty, price])
        print("Product added successfully.")

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
    print("Delete Product")
elif choice == 4:
    print("Update Product")
elif choice == 5:
    print("Search Product")
else:
    print("Invalid Choice")
    