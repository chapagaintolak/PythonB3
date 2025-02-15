shopping_cart = []
<<<<<<< HEAD
total_items = int(input("Enter how many items:"))

for i in range(total_items):
    item = input(f"Enter item {i+1}: ")
    shopping_cart.append(item)

    # display items
print("All items are:  ")
for i in range(total_items):
    print(f"{shopping_cart[i]}")


=======

total_items = int(input("Enter how many items:"))

# You need to purchase 5 items.
for i in range(total_items):
    item = input(f"Enter item: {i+1} ")
    shopping_cart.append(item)

# At the end you need to display all items.

print("All Items are: ")
for i in range(total_items):
    print(f"{shopping_cart[i]}")
>>>>>>> 85a6439a98151d123be4ce9a2879ceac7f8bed13
