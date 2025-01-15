# Random is used to generate random number
# For E.g Luck Based Game, Ludo Dice Roll
import random
print("Flash Card Game")
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

person1name = input("Enter Person 1 Name: ")
person2name = input("Enter Person 2 Name: ")
person3name = input("Enter Person 3 Name: ")

person1 = [random.choice(cards), random.choice(cards), random.choice(cards)]
person2 = [random.choice(cards), random.choice(cards), random.choice(cards)]
person3 = [random.choice(cards), random.choice(cards), random.choice(cards)]

print(f"{person1name} 1 Cards are: {person1}")
print(f"{person2name} Cards are: {person2}")
print(f"{person3name} Cards are: {person3}")