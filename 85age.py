from datetime import date
import calendar

def calculate_age(birth_date):
    today = date.today()
    
    # Calculate years
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1
    
    # Calculate months
    months = today.month - birth_date.month
    if months < 0:
        months += 12
    
    # Calculate days
    if today.day >= birth_date.day:
        days = today.day - birth_date.day
    else:
        # Borrow days from the previous month
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year
        
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days = (today.day + days_in_prev_month) - birth_date.day
        
        # Adjust months
        if months == 0:
            months = 11
        else:
            months -= 1
    
    return years, months, days

birth_date = date(1987, 8, 26)
years, months, days = calculate_age(birth_date)
print(f"Your age is: {years} years, {months} months, {days} days")