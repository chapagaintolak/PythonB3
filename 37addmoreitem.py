print("Welcome to my shopping app.")
total_price = 0
is_shop = True

while is_shop:
    price = float(input("Enter price: "))
    total_price = total_price + price
    
    choice = input("Do you want to add more? [Yes/No]")
    if choice.lower() == "no":
        is_shop = False
        
print(f"Total price is {total_price}")
    
# Write a python program to print 1 to 100 but not 41