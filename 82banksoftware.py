import csv
from turtle import update
from prettytable import PrettyTable
# Create Visitor Entry System For Bank [Nabil Bank]
# ID, Date, Visitor Name, Purpose, 
# Add Following Option
# "1", "Add Visitor"
# "2", "List Visitor"
# "3", "Delete Visitor"
# "4", "Update Visitor"
# "5", "Search Visitor"
# "6", "Show Visitor by ID"
# Start Program

def display_menu():
    print("\nWelcome to Visitor Entry System\n")
    
    menu_table = PrettyTable()
    menu_table.field_names = ["Option", "Description"]
    menu_table.align["Description"] = "l"  # Left align the descriptions

    # Add menu options
    menu_table.add_row(["1", "Add visitor"])
    menu_table.add_row(["2", "List visitor"])
    menu_table.add_row(["3", "Delete visitor"])
    menu_table.add_row(["4", "Update visitort"])
    menu_table.add_row(["5", "Search visitor"])
    menu_table.add_row(["6", "Show visitor by id"])

    print(menu_table)  # Display the menu table
def list_visitor():
    print("List visitor\n")
    # Create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names = ["id", "date", "name", "purpose"]
    table.align["Name"] = "l"
    with open("visitorInformation.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        for line in csv_reader:
            table.add_row([line[0], line[1], line[2], line[3]])  # Add rows to the table
    
    print(table)  # Print table

### Search Product
def search_visitor(nameini):
    print("Search Product\n")
    # Create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names = ["id", "Date", "Name", "Purpose"]
    table.align["Name"] = "l"
    with open('visitorInfo.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[2][0].upper() == nameini[0].upper():
                table.add_row([line[0], line[1], line[2], line[3]])
        print(table)
        print("Product not found.")

# Add Product
def add_visitor(id, date, name, purpose):
    with open('visitorInfo.csv','a',newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([id, date, name, purpose])
        print("visitor added successfully.")

# Show By ID
def show_by_id(id):
    print("Show visitor\n")
    # Create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names = ["id", "date", "name", "purpose"]
    table.align["Name"] = "l"
    with open('visitorInfo.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == id:
                table.add_row([line[0], line[1], line[2], line[3]])
        print(table)

def update_visitor(id):
    print("Previous Record")
    show_by_id(id)
    print("Update Record")
    date = input("Enter update date: ")
    name = input("Enter update Name: ")
    purpose = input("Enter update purpose of the visitor: ")
    
    # Read the CSV file, find the product by id, and update its values
    with open('visitorInfo.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == id:
                row[1] = date
                row[2] = name
                row[3] = purpose
                break
    # Write the updated CSV file
    with open('visitorInfo.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
        print("Visitor information has been updated successfully.")

def delete_visitor(id):
    with open('visitorInfo.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == id:
                rows.remove(row)
                break
    with open('visitorInfo.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
        print("Visitor information has been deleted successfully.")

display_menu()
choice = int(input("Enter your choice: "))
if choice == 1:
    id = input("Enter visitor id: ")
    date = input("Enter Visitor date: ")
    Name = input("Enter visitor Name: ")    
    Purpose = input("Enter Purpose of the visitor: ")
    add_visitor(id, date, Name, Purpose)
elif choice == 2:
    list_visitor()
elif choice == 3:
    id = input("Enter visitor ID: ")
    delete_visitor(id)
elif choice == 4:
    id = input("Enter visitor ID: ")
    update_visitor(id) 
elif choice == 5:
    name = input("Enter visitor Name: ")
    search_visitor(name)
elif choice == 6:
    id = input("Enter visitor ID: ")
    show_by_id(id)
else:
    print("Invalid Choice")
    
    

