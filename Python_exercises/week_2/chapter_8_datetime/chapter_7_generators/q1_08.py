import datetime

def calculate_age(birthdate):
    current_date = datetime.date.today()
    age = current_date.year - birthdate.year
    if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
        age -= 1
    return age


birthdate = datetime.date(1990, 1, 1)
print(calculate_age(birthdate))
