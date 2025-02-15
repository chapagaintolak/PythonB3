name = input("Enter your name: ")
file = open("myname.txt","a")
file.write(f"{name}\n")
file.close()
print("File Write Success")

# Write a program that save your current address on address.txt