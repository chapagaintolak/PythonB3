shopping_cart = []

total_items = int(input("Enter how many items:"))

# You need to purchase 5 items.
for i in range(total_items):
    item = input(f"Enter item: {i+1} ")
    shopping_cart.append(item)

# At the end you need to display all items.

print("All Items are: ")
for i in range(total_items):
    print(f"{shopping_cart[i]}")