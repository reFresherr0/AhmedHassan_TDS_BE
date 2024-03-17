import datetime

def get_weekday(date):
    return date.strftime("%A")

date = datetime.date(2020, 1, 1)
print(get_weekday(date))