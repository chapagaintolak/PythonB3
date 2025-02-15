learn_alphabet = {
    "a": ["Apple", "Ant", "Aeroplane"],
    "b": ["Ball", "Bat", "Boat"],
    "c": ["Cat", "Car", "Cup"],
    "d": ["Dog", "Duck", "Doll"],
    "e": ["Elephant", "Eagle", "Egg"],
    "f": ["Fish", "Frog", "Flower"],
    "g": ["Giraffe", "Guitar", "Grape"],
    "h": ["House", "Horse", "Hamburger"],
    "i": ["Ice Cream", "Igloo", "Island"],
    "j": ["Jacket", "Jelly", "Jet"],
    "k": ["Kangaroo", "Kite", "Koala"],
    "l": ["Lion", "Lipstick", "Lighthouse"],
    "m": ["Monkey", "Mango", "Magnet"],
    "n": ["Nest", "Nose", "Ninja"],
    "o": ["Orange", "Owl", "Octopus"],
    "p": ["Penguin", "Piano", "Panda"],
    "q": ["Queen", "Quill", "Quokka"],
    "r": ["Rabbit", "Rainbow", "Ruler"],
    "s": ["Sun", "Squirrel", "Soccer"],
    "t": ["Tiger", "Tree", "Turtle"],
    "u": ["Umbrella", "Unicorn", "Umbrella"],
    "v": ["Van", "Vase", "Volleyball"],
    "w": ["Watermelon", "Whale", "Watch"],
    "x": ["Xylophone", "X-ray", "Xylophone"],
    "y": ["Yacht", "Yak", "Yogurt"],
    "z": ["Zebra", "Zoo", "Zebra"]
}


user_input = input("Enter a character: ").lower()
if user_input in learn_alphabet:
    print(f"Word start with {user_input} are: ")
    for word in learn_alphabet[user_input]:
        print(f"{user_input.upper()} for {word}")
else:
    print("Invalid input. Please enter a letter.")
