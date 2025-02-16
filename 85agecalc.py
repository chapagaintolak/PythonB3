import datetime
current_year = datetime.datetime.now().year 
current_year = 2025
birth_year= int(input("Enter your birth year: "))
age = current_year - birth_year                 
print(f"Your age is {age}")
