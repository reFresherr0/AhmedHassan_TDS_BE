import datetime

def format_date(date):
    return date.strftime("%B %d, %Y")

date = datetime.date(2020, 1, 1)
print(format_date(date))