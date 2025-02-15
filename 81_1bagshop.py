import csv
#pip install prettyTable
from prettytable import PrettyTable

def display_menu():
    """Display the menu options in a PrettyTable format."""
    print("\nWelcome to ABC Bagshop Software\n")

    menu_table = PrettyTable()
    menu_table.field_names = ["Option", "Description"]
    menu_table.align["Description"] = "l" # left align the description

    # add menu options
    menu_table.add_row(["1", "Add Product"])
    menu_table.add_row(["2", "List Product"])
    menu_table.add_row(["3", "Delet Product"])
    menu_table.add_row(["4", "Update Product"])
    menu_table.add_row(["5", "Search Product"])

    print(menu_table) # Display the menu table
    
def list_product():
    print("List Product\n")

    # create a prettyTable instance
    table = PrettyTable()

   ############# define the colum names ################
    table.field_names = ["id", "name", "qty", "price", "total"]
    table.align["name"] = "l"

    with open("bag_shop_data.csv", "r") as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            table.add_row([line[0], line[1], line[2], line[3], float(line[2])*float(line[3])])
    
    print(table) # print table

########### add product ############################
def add_product(id, name, qty, price):
    with open("bag_shop_data.csv", "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([id, name, qty, price])
        print("product added successfully")

############## delete product ############################
def update_product(id):
    print("Previous records")
    show_by_id(id)  # show the product details
    print("Update record")
    name = input("Enter new Name: ")
    qty = input("Enter new Quantity: ")
    price = input("Enter new Price: ") 

    with open("bag_shop_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == id:
                row[1] = name
                row[2] = qty
                row[3] = price
                break
    with open("bag_shop_data.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)  
        print("Product updated successfully")





############# delect product ############################
def delete_product(id):
    with open("bag_shop_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == id:
                rows.remove(row)
                break
    with open("bag_shop_data.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
        print("Product deleted successfully.")


### #####Show By id ##########################3
def show_by_id(id):
    print("show Product\n")
    # create a PrettyTable instance
    table = PrettyTable()
    # Define the column names
    table.field_names=["id", "name", "qty", "price", "total"]
    table.align["Name"] = "l"
    with open ('bag_shop_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0]==id:
                table.add_row([line[0], line[1], line[2], line[3], float(line[2])*float(line[3])])
            print(table)
            

###########3 search product
def search_product(nameini):
    print("Search Product\n")

    # Create a prettyTable instance
    table = PrettyTable()
    table.field_names=["id", "name", "qty", "price", "total"]
    table.align["name"] = "l"
    with open("bag_shop_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[1][0].upper() == nameini[0].upper():
                table.add_row([line[0], line[1], line[2], line[3], float(line[2])*float(line[3])])
        print(table)
        print("Product not found")

        
display_menu()

choice = int(input("Enter your choice: "))

if choice == 1:
    id = input("Enter product ID: ")
    name = input("Enter product Name: ")
    qty = input("Enter product Quantity: ")
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