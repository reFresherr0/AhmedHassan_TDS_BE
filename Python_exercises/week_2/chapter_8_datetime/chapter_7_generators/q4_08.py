import calendar

def is_leap_year(year):
    return calendar.isleap(year)

leap_year = is_leap_year(2020)
print(leap_year)