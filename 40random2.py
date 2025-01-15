import random
print("Fruit Game")
# 5 Fruits 3 Person
fruits = ['Apple', 'Orange', 'Mango', 'Banana', 'Grapes']

print(f"All Fruits: {fruits}")

fruits_for_person1 = random.choice(fruits)
print(f"Person 1 got: {fruits_for_person1}")
fruits.remove(fruits_for_person1)

fruits_for_person2 = random.choice(fruits)
print(f"Person 2 got: {fruits_for_person2}")
fruits.remove(fruits_for_person2)

fruits_for_person3 = random.choice(fruits)
print(f"Person 3 got: {fruits_for_person3}")
fruits.remove(fruits_for_person3)

print(f"Available Fruits: {fruits}")