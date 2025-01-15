print("Welcome to my shopping app.")
total_items = int(input("Enter how many items: "))
total_price = 0

for i in range(1,total_items+1):
    price = float(input(f"Enter price for {i}: "))
    total_price = total_price + price

print(f"Total price is {total_price}")
