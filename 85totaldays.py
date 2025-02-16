### create porgram that find total years, Days, Hour, min second
# Enter your birth year, month, day
# Calculate it
# Total years: 6
# Total days: 
# Total hours:
# Total minutes:
# Total seconds:

## Create function called add(), sub(), mul(), div()
## Test the program using pytest
## At atleast 5 test case for each function.


import datetime
current_year = datetime.datetime.now().year         
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day  
current_hour = datetime.datetime.now().hour
current_minute = datetime.datetime.now().minute
current_second = datetime.datetime.now().second
current_microsecond = datetime.datetime.now().microsecond

print(f"Current year: {current_year}")         
birth_year= int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))
age = current_year - birth_year                 
print(f"Your age is {age}") 
total_days = (current_year - birth_year) * 365
print(f"Total days: {total_days}")  
total_hours = (current_year - birth_year) * 365 * 24
print(f"Total hours: {total_hours}")
total_minutes = (current_year - birth_year) * 365 * 24 * 60
print(f"Total minutes: {total_minutes}")
total_seconds = (current_year - birth_year) * 365 * 24 * 60 * 60
print(f"Total seconds: {total_seconds}")
total_microseconds = (current_year - birth_year) * 365 * 24 * 60 * 60 * 1000000
print(f"Total microseconds: {total_microseconds}")  


# print  my age in years-monts-days


print(f"your age is {age} years, {current_month - birth_month} months, {current_day - birth_day} days")
# print  my age in years-monts-days



















