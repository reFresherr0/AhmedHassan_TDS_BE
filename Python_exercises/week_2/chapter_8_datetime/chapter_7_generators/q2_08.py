from datetime import datetime

def calculate_days(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start
    return delta.days

start_date = "2020-01-01"
end_date = "2020-01-31"
print(calculate_days(start_date, end_date))