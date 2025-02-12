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
