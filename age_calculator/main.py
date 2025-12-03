from datetime import date

def age_calculator(d, m, y):
    today = date.today()
    dob = date(y, m, d)
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day
    if days < 0:
        months -= 1
        previous_month = today.month - 1 or 12
        previous_year = today.year if today.month > 1 else today.year - 1
        days += (date(previous_year, previous_month + 1, 1) - 
                 date(previous_year, previous_month, 1)).days
    if months < 0:
        years -= 1
        months += 12
    return years, months, days
def main():
    d = int(input("Enter birth day (DD): "))
    m = int(input("Enter birth month (MM): "))
    y = int(input("Enter birth year (YYYY): "))
    years, months, days = age_calculator(d, m, y)
    print(f"\nYour Age: {years} years, {months} months, {days} days")
main()
