birthyear = int(input("Enter your birth year: "))
age = 2025 - birthyear

if age >= 18:
    print("You are voter")
    print("You can vote")
else:
    print("You are not voter")
    print("You can not vote")

print("Program completed.")