shopping_cart = []
total_items = int(input("Enter how many items:"))

for i in range(total_items):
    item = input(f"Enter item {i+1}: ")
    shopping_cart.append(item)

    # display items
print("All items are:  ")
for i in range(total_items):
    print(f"{shopping_cart[i]}")


