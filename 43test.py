import random
print ("Three Lucky Winners")

f = open("names.txt", "r")

names = f.readlines()
for i in range(len(names)):
    names[i] = names[i].strip("\n")
    
winner1 = random.choice(names)
names.remove(winner1)

winner2 = random.choice(names)
names.remove(winner2)

winner3 = random.choice(names)
names.remove(winner3)

print(f"First Winner is: {winner1}")
print(f"Second Winner is: {winner2}")
print(f"Third Winner is: {winner3}")