name = input("Enter your name: ")
address = input("Enter your address: ")
file = open("myaddress.txt","a")
file.write(f"Name: {name}\n")
file.write(f"Address:  {address}\n")
file.close()
print("File Write Successfully")

