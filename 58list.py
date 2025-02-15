<<<<<<< HEAD
names = ["Binaya", "Bishal", "Bikash"]
names.append("Bibek")
print(names)
names.append("Ravi")
print(names)


if "Binaya" in names:
    print("Binaya is in the list")
else:
    print("Binaya is not in the list")

names.remove("Bishal")
print(names)

########## Total names ###################3
total_names = len(names)
print(f"Total names are: {total_names}")

print (type(names))

print(names[1])
print(names[-1])
print(names[:-1])
print(names[::-1])
print(names[1:3])
print(names[1:])

names = ["Binaya", "Bishal", "Bikash"]
names.insert(1, "Ravi")
print(names)
names[0]="Kiran"
print(names)

for n in names:
    print(n)

for i in range(len(names)):
    print(f"{i+1}. Name is: {names[i]}") 
=======
names = ["Binaya Shrestha", "Dilip Karki", "Diwash"]

names.insert(1, "Kishor Saud")
# for n in names:
#     print(n)

# for i in range(len(names)):
#     print(f"Name: {names[i]}")


# if "Diwash" in names:
#     print("Diwash is in the list")
# else:
#     print("Diwash is not in the list")
# # names.append("Kishor Saud")


# total_names = len(names)

# print(f"Total names: {total_names}")
>>>>>>> 85a6439a98151d123be4ce9a2879ceac7f8bed13
