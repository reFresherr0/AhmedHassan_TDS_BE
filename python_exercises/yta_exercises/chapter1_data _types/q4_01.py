import datetime    #importing datetime module

age_years = int(input("How old are you? "))
curr_Year = datetime.date.today().year
user_BirthYear = curr_Year-age_years    #calculating birth year

print("You were born in the year: " + str(user_BirthYear))